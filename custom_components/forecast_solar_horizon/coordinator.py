"""DataUpdateCoordinator for the Forecast.Solar.Horizon integration."""

from __future__ import annotations

from datetime import timedelta

from forecast_solar import Estimate, ForecastSolar, ForecastSolarConnectionError

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_API_KEY, CONF_LATITUDE, CONF_LONGITUDE
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    CONF_AZIMUTH,
    CONF_DAMPING_EVENING,
    CONF_DAMPING_MORNING,
    CONF_DECLINATION,
    CONF_HORIZON,
    CONF_INVERTER_SIZE,
    CONF_MODULES_POWER,
    DOMAIN,
    LOGGER,
)

type ForecastSolarConfigEntry = ConfigEntry[ForecastSolarDataUpdateCoordinator]


class ForecastSolarDataUpdateCoordinator(DataUpdateCoordinator[Estimate]):
    """The Forecast.Solar.Horizon Data Update Coordinator."""

    config_entry: ForecastSolarConfigEntry

    def __init__(self, hass: HomeAssistant, entry: ForecastSolarConfigEntry) -> None:
        """Initialize the Forecast.Solar.Horizon coordinator."""

        # Our option flow may cause it to be an empty string,
        # this if statement is here to catch that.
        api_key = entry.options.get(CONF_API_KEY) or None

        if (
            inverter_size := entry.options.get(CONF_INVERTER_SIZE)
        ) is not None and inverter_size > 0:
            inverter_size = inverter_size / 1000

        self.forecast = ForecastSolar(
            api_key=api_key,
            session=async_get_clientsession(hass),
            latitude=entry.data[CONF_LATITUDE],
            longitude=entry.data[CONF_LONGITUDE],
            declination=entry.options[CONF_DECLINATION],
            azimuth=(entry.options[CONF_AZIMUTH] - 180),
            kwp=(entry.options[CONF_MODULES_POWER] / 1000),
            damping_morning=entry.options.get(CONF_DAMPING_MORNING, 0.0),
            damping_evening=entry.options.get(CONF_DAMPING_EVENING, 0.0),
            inverter=inverter_size,
            horizon=entry.options.get(CONF_HORIZON, None),
        )

        # Free account have a resolution of 1 hour, using that as the default
        # update interval. Using a higher value for accounts with an API key.
        update_interval = timedelta(hours=1)
        if api_key is not None:
            update_interval = timedelta(minutes=30)

        super().__init__(
            hass,
            LOGGER,
            config_entry=entry,
            name=DOMAIN,
            update_interval=update_interval,
        )

    async def _async_update_data(self) -> Estimate:
        """Fetch Forecast.Solar.Horizon estimates."""
        try:
            return await self.forecast.estimate()
        except ForecastSolarConnectionError as error:
            raise UpdateFailed(error) from error
