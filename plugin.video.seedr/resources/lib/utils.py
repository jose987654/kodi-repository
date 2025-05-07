# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import sys
import logging
import routing
import json
import urllib.parse
from xbmcgui import ListItem

# Addon info
ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_PATH = ADDON.getAddonInfo('path')
ADDON_VERSION = ADDON.getAddonInfo('version')

# Setup logging
logger = logging.getLogger(ADDON_ID)

class KodiLogHandler(logging.StreamHandler):
    def __init__(self):
        logging.StreamHandler.__init__(self)
        prefix = b"[%s] " % ADDON_ID
        formatter = logging.Formatter(prefix + b'%(name)s: %(message)s')
        self.setFormatter(formatter)

    def emit(self, record):
        levels = {
            logging.CRITICAL: xbmc.LOGFATAL,
            logging.ERROR: xbmc.LOGERROR,
            logging.WARNING: xbmc.LOGWARNING,
            logging.INFO: xbmc.LOGINFO,
            logging.DEBUG: xbmc.LOGDEBUG,
            logging.NOTSET: xbmc.LOGNONE,
        }
        if get_setting_as_bool('debug'):
            try:
                xbmc.log(self.format(record), levels[record.levelno])
            except UnicodeEncodeError:
                xbmc.log(self.format(record).encode('utf-8', 'ignore'), levels[record.levelno])

    def flush(self):
        pass

def setup_logging():
    """Configure logging for the addon"""
    logger = logging.getLogger()
    logger.addHandler(KodiLogHandler())
    logger.setLevel(logging.DEBUG)

# Settings functions
def get_setting(setting):
    """Get addon setting"""
    return ADDON.getSetting(setting).strip().decode('utf-8')

def set_setting(setting, value):
    """Set addon setting"""
    ADDON.setSetting(setting, str(value))

def get_setting_as_bool(setting):
    """Get setting as boolean"""
    return get_setting(setting).lower() == "true"

def get_setting_as_float(setting):
    """Get setting as float"""
    try:
        return float(get_setting(setting))
    except ValueError:
        return 0

def get_setting_as_int(setting):
    """Get setting as integer"""
    try:
        return int(get_setting_as_float(setting))
    except ValueError:
        return 0

def get_string(string_id):
    """Get localized string"""
    return ADDON.getLocalizedString(string_id).encode('utf-8', 'ignore')

def show_settings():
    """Open addon settings"""
    ADDON.openSettings()

# UI functions
def notification(header, message, time=5000, icon=ADDON.getAddonInfo('icon'), sound=True):
    """Show Kodi notification"""
    xbmcgui.Dialog().notification(header, message, icon, time, sound)

def show_error(message):
    """Show error dialog"""
    xbmcgui.Dialog().ok(ADDON_NAME, message)

def show_yes_no(message):
    """Show yes/no dialog"""
    return xbmcgui.Dialog().yesno(ADDON_NAME, message)

# Plugin routing
plugin = routing.Plugin()

def add_directory_item(url, list_item, is_folder=True):
    """Add item to directory listing"""
    xbmcplugin.addDirectoryItem(plugin.handle, url, list_item, is_folder)

def end_of_directory():
    """End directory listing"""
    xbmcplugin.endOfDirectory(plugin.handle)

def set_content(content):
    """Set content type"""
    xbmcplugin.setContent(plugin.handle, content)

def set_plugin_category(category):
    """Set plugin category"""
    xbmcplugin.setPluginCategory(plugin.handle, category)

def add_sort_method(method):
    """Add sort method"""
    xbmcplugin.addSortMethod(plugin.handle, method)

# JSON-RPC functions
def kodi_json_request(params):
    """Make JSON-RPC request to Kodi"""
    data = json.dumps(params)
    request = xbmc.executeJSONRPC(data)

    try:
        response = json.loads(request)
    except UnicodeDecodeError:
        response = json.loads(request.decode('utf-8', 'ignore'))

    try:
        if 'result' in response:
            return response['result']
        return None
    except KeyError:
        logger.warn("[%s] %s" % (params['method'], response['error']['message']))
        return None

# URL handling
def build_url(**kwargs):
    """Build plugin URL with parameters"""
    return '{0}?{1}'.format(plugin.url_for('index'), urllib.parse.urlencode(kwargs))

# Plugin routes
@plugin.route('/')
def index():
    """Main menu"""
    set_plugin_category('Seedr')
    set_content('videos')
    
    # Add main menu items
    categories = [
        ('My Files', 'files'),
        ('Recent', 'recent'),
        ('Favorites', 'favorites')
    ]
    
    for name, category in categories:
        list_item = ListItem(label=name)
        list_item.setInfo('video', {'title': name})
        url = plugin.url_for('show_category', category=category)
        add_directory_item(url, list_item, True)
    
    add_sort_method(xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    end_of_directory()

@plugin.route('/category/<category>')
def show_category(category):
    """Show category content"""
    set_plugin_category(category)
    set_content('videos')
    
    # Here you would implement the actual Seedr API calls
    # This is just a placeholder
    videos = [
        ('Sample Video 1', 'video1.mp4'),
        ('Sample Video 2', 'video2.mp4')
    ]
    
    for name, video_id in videos:
        list_item = ListItem(label=name)
        list_item.setInfo('video', {'title': name})
        list_item.setProperty('IsPlayable', 'true')
        url = plugin.url_for('play_video', video=video_id)
        add_directory_item(url, list_item, False)
    
    add_sort_method(xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    end_of_directory()

@plugin.route('/play/<video_id>')
def play_video(video_id):
    """Play video"""
    # Here you would implement the actual video playback
    # This is just a placeholder
    logger.info(f"Playing video: {video_id}")
    notification(ADDON_NAME, 'Video playback not implemented yet')

def run():
    """Run the plugin"""
    setup_logging()
    plugin.run() 