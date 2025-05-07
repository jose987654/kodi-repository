# Seedr Kodi Addon

A Kodi addon that allows you to access and stream your Seedr.cc cloud storage content directly through Kodi.

## What is Kodi?

Kodi is a free and open-source media player software application developed by the XBMC Foundation. It's a powerful entertainment hub that allows you to:

- Play and view most videos, music, podcasts, and other digital media files
- Organize and manage your media library
- Stream content from the internet
- Customize your experience with addons and skins
- Run on multiple platforms including Windows, macOS, Linux, Android, and iOS

Kodi is particularly popular among home theater enthusiasts and cord-cutters as it provides a unified interface for accessing various media sources, including local storage, network drives, and online services like Seedr.cc.

## Features

- Browse your Seedr.cc cloud storage folders and files
- Stream video and audio content directly in Kodi
- Automatic authentication with Seedr.cc
- Support for video thumbnails and metadata
- Folder navigation with context menu options

## Requirements

- Kodi media center
- Seedr.cc account
- Internet connection

## Installation

1. Download the addon zip file
2. In Kodi, go to Add-ons > Install from zip file
3. Select the downloaded zip file
4. The addon will be installed and available in your Kodi addons

## First-time Setup

1. Launch the addon from Kodi
2. You will be presented with a verification URL and code
3. Visit the provided URL in your web browser
4. Enter the verification code
5. The addon will automatically complete the authentication process

## Usage

- Navigate through your Seedr.cc folders using the Kodi interface
- Video files will be automatically playable
- Audio files will be available for streaming
- Use the context menu to refresh the current view or go back to parent directory

## Technical Details

The addon uses the Seedr.cc API to:

- Authenticate users through device code flow
- List folders and files
- Stream media content
- Display thumbnails and metadata

## Development Dependencies

- Python 2.7 or 3.x
- Kodi addon development environment with Python API (`xbmc`, `xbmcaddon`, `xbmcgui`, `xbmcplugin`)
- `script.module.routing` (Kodi addon dependency)

## Development Setup

### Installing Kodi for Development

1. Download and install Kodi from [kodi.tv/download](https://kodi.tv/download)
2. For Windows:
   - Default installation path: `C:\Program Files\Kodi`
   - Python libraries are located at: `C:\Program Files\Kodi\system\python`
3. For Linux:
   - Install via package manager: `sudo apt install kodi`
   - Python libraries are typically at: `/usr/lib/x86_64-linux-gnu/kodi/system/python`

### Setting Up Python Path

1. Add Kodi's Python libraries to your Python path:

   ```bash
   # Windows (PowerShell)
   $env:PYTHONPATH += ";C:\Program Files\Kodi\system\python"

   # Linux
   export PYTHONPATH=$PYTHONPATH:/usr/lib/x86_64-linux-gnu/kodi/system/python
   ```

2. Verify the setup by running Python and trying to import Kodi modules:
   ```python
   import xbmcplugin
   import xbmcgui
   ```

### Installing Required Addons

1. Install `script.module.routing`:
   - In Kodi, go to Add-ons > Install from repository
   - Select Kodi Add-on repository
   - Go to Program add-ons
   - Find and install `script.module.routing`

## Support

For issues or questions, please check the project's issue tracker or contact the maintainers.

## License

[Add license information here]
