# Forecast Solar Horizon

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

A custom component for Home Assistant that provides solar production forecasts with horizon support. This is a fork of the official [Forecast.Solar integration](https://www.home-assistant.io/integrations/forecast_solar/) with added horizon profile support.

Solves:

- https://github.com/home-assistant/core/pull/113894
- https://github.com/home-assistant/core/pull/78326

## Features

- Provides solar production forecasts based on your solar panel configuration
- Supports horizon profiles to account for obstacles blocking sunlight
- Offers various sensors for energy production estimates (today, tomorrow, hourly)
- Provides power production estimates (now, next hour, etc.)
- Integrates with Home Assistant Energy Dashboard

## Installation

### HACS Installation (Recommended)

1. Make sure you have [HACS](https://hacs.xyz/) installed
2. Go to HACS → Integrations → Click the three dots in the top right corner → Custom repositories
3. Add this repository URL: `https://github.com/LustigePerson/forecast_solar_horizon`
4. Select "Integration" as the category
5. Click "Add"
6. Search for "Forecast Solar Horizon" in the HACS Integrations page
7. Click "Install"
8. Restart Home Assistant

### Manual Installation

1. Download the latest release from the [GitHub repository](https://github.com/LustigePerson/forecast_solar_horizon)
2. Extract the `custom_components/forecast_solar_horizon` directory to your Home Assistant's `custom_components` directory
3. Restart Home Assistant

## Configuration

This integration can be configured through the Home Assistant UI:

1. Go to **Settings** → **Devices & Services**
2. Click the **+ Add Integration** button
3. Search for "Forecast Solar Horizon" and select it
4. Follow the configuration steps:
   - Enter a name for the integration
   - Confirm or adjust the latitude and longitude
   - Enter the declination angle of your solar panels (0 = horizontal, 90 = vertical)
   - Enter the azimuth angle (0 = North, 90 = East, 180 = South, 270 = West)
   - Enter the total watt peak power of your solar modules

### Advanced Configuration

After the initial setup, you can configure additional options:

1. Go to **Settings** → **Devices & Services**
2. Find the "Forecast Solar Horizon" integration and click "Configure"
3. Additional options include:
   - API key (optional, for premium features)
   - Damping factors for morning and evening
   - Inverter size
   - Horizon profile (comma-separated list of degrees, e.g., "0,0,25,30,20,10,0")

## Horizon Profile

The horizon profile is a comma-separated list of degrees that represents obstacles blocking sunlight at different azimuth angles. This is particularly useful if you have buildings, trees, or mountains that block the sun at certain times of the day.

The format follows the PVGIS standard, with values representing elevation angles at regular azimuth intervals. For example, "0,0,25,30,20,10,0" would represent:

- 0° elevation at the first azimuth point
- 0° elevation at the second azimuth point
- 25° elevation at the third azimuth point
- etc.

## Available Sensors

This integration provides the following sensors:

- Estimated energy production - today
- Estimated energy production - remaining today
- Estimated energy production - tomorrow
- Highest power peak time - today
- Highest power peak time - tomorrow
- Estimated power production - now
- Estimated power production - next hour
- Estimated power production - next 12 hours
- Estimated power production - next 24 hours
- Estimated energy production - this hour
- Estimated energy production - next hour

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
