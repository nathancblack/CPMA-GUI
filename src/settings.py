# src/settings.py
# This file contains the definitions for all configurable settings.
# "value" starts as None and should be populated by the config reader.

# --- 1. MOUSE SETTINGS ---
MOUSE_SETTINGS = {
    "in_mouse": {
        "value": None,
        "type": "discrete",
        "options": ["0", "1", "2"],
        "game_default": "1",
        "description": "Mouse input mode. 0 = Disabled, 1 = Raw input, 2 = Win32 input",
        "label": "Mouse Input Mode"
    },
    "m_filter": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Mouse smoothing.",
        "label": "Mouse Smoothing"
    },
    "m_speed": {
        "value": None,
        "type": "float",
        "min": 0.0,
        "max": 100.0,
        "game_default": "2",
        "description": "Mouse sensitivity.",
        "label": "Sensitivity"
    },
    "m_yaw": {
        "value": None,
        "type": "float",
        "min": -100.0,
        "max": 100.0,
        "game_default": "0.022",
        "description": "Post-accel horizontal mouse sensitivity.",
        "label": "Yaw"
    },
    "m_pitch": {
        "value": None,
        "type": "float",
        "min": -100.0,
        "max": 100.0,
        "game_default": "0.022",
        "description": "Post-accel vertical mouse sensitivity.",
        "label": "Pitch"
    },
    "m_accel": {
        "value": None,
        "type": "float",
        "min": 0.0,
        "max": 1000.0, # +inf in file, set reasonable cap
        "game_default": "0",
        "description": "Mouse acceleration.",
        "label": "Acceleration"
    },
    "m_accelStyle": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "0 = original, 1 = new.",
        "label": "Acceleration Style"
    },
    "m_accelOffset": {
        "value": None,
        "type": "float",
        "min": 0.001,
        "max": 5000.0,
        "game_default": "5",
        "description": "Offset for the power function. For m_accelStyle 1 only.",
        "label": "Acceleration Offset"
    },
    "m_limit": {
        "value": None,
        "type": "float",
        "min": 0.0,
        "max": 1000.0, # +inf in file
        "game_default": "0",
        "description": "Mouse speed cap (0=disabled).",
        "label": "Speed Limit"
    },
    "cl_drawMouseLag": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Draws sampling to display/upload delays.",
        "label": "Draw Mouse Lag"
    },
    "com_maxfps": {
        "value": None,
        "type": "int",
        "min": 60,
        "max": 250,
        "game_default": "125",
        "description": "Max allowed framerate. It's highly recommended to only use 125 or 250 with V-Sync disabled.",
        "label": "Max FPS"
    }
}

# --- 2. VIDEO SETTINGS ---
VIDEO_SETTINGS = {
    "r_gamma": {
        "value": None,
        "type": "float",
        "min": 0.5,
        "max": 3.0,
        "game_default": "1.2",
        "description": "Gamma correction factor. <1 = Darker, 1 = No change, >1 = Brighter",
        "label": "Gamma"
    },
    "r_intensity": {
        "value": None,
        "type": "float",
        "min": 1.0,
        "max": 3.0, # +inf in file
        "game_default": "1",
        "description": "Brightness of non-lightmap map textures.",
        "label": "Intensity"
    },
    "r_greyscale": {
        "value": None,
        "type": "float",
        "min": 0.0,
        "max": 1.0,
        "game_default": "0",
        "description": "How desaturated the final image looks.",
        "label": "Greyscale"
    },
    "r_fullbright": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Renders the diffuse textures only. Shaders with a lightmap stage will not draw the lightmap stage. Mutually exclusive with r_lightmap.",
        "label": "Fullbright"
    },
    "r_brightness": {
        "value": None,
        "type": "float",
        "min": 0.25,
        "max": 32.0,
        "game_default": "2",
        "description": "Overall brightness.",
        "label": "Brightness"
    },
    "r_mapBrightness": {
        "value": None,
        "type": "float",
        "min": 0.25,
        "max": 32.0,
        "game_default": "2",
        "description": "Brightness of lightmap textures.",
        "label": "Map Brightness"
    },
    "r_vertexLight": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Disables lightmap texture blending.",
        "label": "Vertex Light"
    },
    "r_dynamiclight": {
        "value": None,
        "type": "bool",
        "game_default": "1",
        "description": "Enables dynamic lights.",
        "label": "Dynamic Light"
    },
    "r_lightmap": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Renders the lightmaps only. Mutually exclusive with r_fullbright.",
        "label": "Lightmap"
    },
    "r_fastsky": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Makes the sky and portals pure black.",
        "label": "Fast Sky"
    },
    "r_noportals": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Disables rendering of portals.",
        "label": "No Portals"
    },
    "r_ext_max_anisotropy": {
        "value": None,
        "type": "int",
        "min": 0,
        "max": 16,
        "game_default": "16",
        "description": "Max allowed anisotropy ratio. Needs to be 2 or higher to be enabled.",
        "label": "Max Anisotropy"
    },
    "r_textureMode": {
        "value": None,
        "type": "string",
        "game_default": "best",
        "description": "Texture filtering mode. GL_NEAREST = LEGO mode, anything else = Normal.",
        "label": "Texture Mode"
    },
    "r_picmip": {
        "value": None,
        "type": "int",
        "min": 0,
        "max": 16,
        "game_default": "0",
        "description": "Lowest allowed mip level. Lower number means sharper textures.",
        "label": "Picmip"
    },
    "r_detailtextures": {
        "value": None,
        "type": "bool",
        "game_default": "1",
        "description": "Enables detail textures shader stages.",
        "label": "Detail Textures"
    },
    "r_colorMipLevels": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Colorizes textures based on their mip level.",
        "label": "Color Mip Levels"
    },
    "r_teleporterFlash": {
        "value": None,
        "type": "bool",
        "game_default": "1",
        "description": "Draws bright colors when being teleported.",
        "label": "Teleporter Flash"
    },
    "r_monitor": {
        "value": None,
        "type": "int",
        "min": 0,
        "max": 4,
        "game_default": "0",
        "description": "1-based monitor index. 0=primary.",
        "label": "Monitor"
    },
    "r_fullscreen": {
        "value": None,
        "type": "bool",
        "game_default": "1",
        "description": "Full-screen mode.",
        "label": "Fullscreen"
    },
    "r_blitMode": {
        "value": None,
        "type": "discrete",
        "options": ["0", "1", "2"],
        "game_default": "0",
        "description": "Image upscaling mode. 0=Aspect-ratio preserving, 1=No scaling, 2=Stretching.",
        "label": "Blit Mode"
    },
    "r_mode": {
        "value": None,
        "type": "discrete",
        "options": ["0", "1", "2"],
        "game_default": "0",
        "description": "Video mode. 0=Desktop res, 1=Custom res (no change), 2=Custom res (change mode).",
        "label": "Video Mode"
    },
    "r_width": {
        "value": None,
        "type": "int",
        "min": 320,
        "max": 65535,
        "game_default": "1280",
        "description": "Custom window/render width.",
        "label": "Width"
    },
    "r_height": {
        "value": None,
        "type": "int",
        "min": 240,
        "max": 65535,
        "game_default": "720",
        "description": "Custom window/render height.",
        "label": "Height"
    },
    "r_customaspect": {
        "value": None,
        "type": "int",
        "min": 0,
        "max": 10,
        "game_default": "1",
        "description": "Custom pixel aspect ratio.",
        "label": "Custom Aspect"
    },
    "r_displayRefresh": {
        "value": None,
        "type": "int",
        "min": 0,
        "max": 480,
        "game_default": "0",
        "description": "Desirable refresh rate. 0 lets the driver decide.",
        "label": "Display Refresh"
    },
    "r_swapInterval": {
        "value": None,
        "type": "int",
        "min": -8,
        "max": 8,
        "game_default": "0",
        "description": "V-Sync. 0=Off, >0=Standard, <0=Adaptive.",
        "label": "V-Sync"
    },
    "r_msaa": {
        "value": None,
        "type": "int",
        "min": 0,
        "max": 32,
        "game_default": "0",
        "description": "Anti-aliasing sample count. 0=off.",
        "label": "MSAA"
    },
    "r_lodbias": {
        "value": None,
        "type": "int",
        "min": -16,
        "max": 16,
        "game_default": "-2",
        "description": "MD3 models LOD bias. A higher number means higher quality loss.",
        "label": "LOD Bias"
    }
}

# --- 3. AUDIO SETTINGS ---
AUDIO_SETTINGS = {
    "s_autoMute": {
        "value": None,
        "type": "discrete",
        "options": ["0", "1", "2"],
        "game_default": "1",
        "description": "When audio should be disabled. 0=Never, 1=Unfocused, 2=Minimized.",
        "label": "Auto Mute"
    },
    "s_volume": {
        "value": None,
        "type": "float",
        "min": 0.0,
        "max": 1.0,
        "game_default": "0.2",
        "description": "Global sound volume.",
        "label": "Volume"
    },
    "s_musicvolume": {
        "value": None,
        "type": "float",
        "min": 0.0,
        "max": 16.0,
        "game_default": "0",
        "description": "Music volume.",
        "label": "Music Volume"
    },
    "s_ambient": {
        "value": None,
        "type": "bool",
        "game_default": "1",
        "description": "Enables maps ambient sounds.",
        "label": "Ambient Sounds"
    },
    "s_announcer": {
        "value": None,
        "type": "string",
        "game_default": "feedback",
        "description": "Announcer sound pack (e.g., feedback, hellchick).",
        "label": "Announcer"
    },
    "cg_oldCTFSounds": {
        "value": None,
        "type": "discrete",
        "options": ["0", "1", "2"],
        "game_default": "2",
        "description": "CTF sounds. 0=TA sounds, 1=Q3 1.17 sounds, 2=Team-specific sounds.",
        "label": "CTF Sounds"
    },
    "cg_noteamchatbeep": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Disables team chat beep sounds.",
        "label": "No Team Chat Beep"
    },
    "cg_nochatbeep": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Disables chat beep sounds.",
        "label": "No Chat Beep"
    },
    "cg_noTaunt": {
        "value": None,
        "type": "bool",
        "game_default": "1",
        "description": "Disable all taunts, not just voice chat ones.",
        "label": "No Taunt"
    },
    "cg_noHitBeep": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Disables hit beeps.",
        "label": "No Hit Beep"
    }
}

# --- 4. HUD & UI SETTINGS ---
HUD_SETTINGS = {
    "cg_drawCrosshair": {
        "value": None,
        "type": "int",
        "min": 0,
        "max": 20,
        "game_default": "11",
        "description": "Crosshair visual style (0-20).",
        "label": "Crosshair"
    },
    "cg_crosshairX": {
        "value": None,
        "type": "int",
        "min": -320,
        "max": 320,
        "game_default": "0",
        "description": "X-axis offset from screen center.",
        "label": "Crosshair X"
    },
    "cg_crosshairY": {
        "value": None,
        "type": "int",
        "min": -240,
        "max": 240,
        "game_default": "0",
        "description": "Y-axis offset from screen center.",
        "label": "Crosshair Y"
    },
    "cg_crosshairSize": {
        "value": None,
        "type": "string",
        "game_default": "26x32",
        "description": "Crosshair scale (e.g., '24' or '24x24').",
        "label": "Crosshair Size"
    },
    "cg_crosshairHealth": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Sets crosshair color based on your stack.",
        "label": "Crosshair Health"
    },
    "ch_crosshairAlpha": {
        "value": None,
        "type": "float",
        "min": 0.0,
        "max": 1.0,
        "game_default": "1",
        "description": "Crosshair opacity.",
        "label": "Crosshair Alpha"
    },
    "ch_crosshairColor": {
        "value": None,
        "type": "string",
        "game_default": "7",
        "description": "Crosshair color code [0-9a-z].",
        "label": "Crosshair Color"
    },
    "ch_crosshairHitColor": {
        "value": None,
        "type": "string",
        "game_default": "",
        "description": "Crosshair color after hitting an enemy. Leave empty to disable.",
        "label": "Crosshair Hit Color"
    },
    "ch_crosshairPulse": {
        "value": None,
        "type": "discrete",
        "options": ["0", "1", "2", "3"],
        "game_default": "0",
        "description": "Crosshair pulse events. 0=Never, 1=Pickup, 2=Damage, 3=Frags.",
        "label": "Crosshair Pulse"
    },
    "ch_file": {
        "value": None,
        "type": "string",
        "game_default": "hud",
        "description": "Name of the SuperHUD config file in cpma/hud.",
        "label": "HUD File"
    },
    "ch_drawKeys": {
        "value": None,
        "type": "bitmask",
        "game_default": "0",
        "description": "Enables KeyDown/Up elements. 1=Playing, 2=Following, 4=Demos.",
        "label": "Draw Keys"
    },
    "cg_drawCrosshairNames": {
        "value": None,
        "type": "discrete",
        "options": ["0", "1", "2"],
        "game_default": "1",
        "description": "Draws target name. 0=Disabled, 1=Enabled, 2=Teammates only.",
        "label": "Draw Crosshair Names"
    }
}

# --- 5. PLAYER SETTINGS ---
PLAYER_SETTINGS = {
    "name": {
        "value": None,
        "type": "string",
        "game_default": "UnnamedPlayer",
        "description": "Your name.",
        "label": "Name"
    },
    "nick": {
        "value": None,
        "type": "string",
        "game_default": "Short Name",
        "description": "Short name (max 5 chars) for team overlay.",
        "label": "Nickname"
    },
    "color": {
        "value": None,
        "type": "string",
        "game_default": "17770",
        "description": "Player colors (CHBLS). Example: 17770",
        "label": "Color"
    },
    "model": {
        "value": None,
        "type": "string",
        "game_default": "mynx/pm",
        "description": "Your own player model.",
        "label": "Model"
    },
    "cg_showPlayerLean": {
        "value": None,
        "type": "bool",
        "game_default": "1",
        "description": "Enables player model leaning.",
        "label": "Show Player Lean"
    },
    "cg_forceModel": {
        "value": None,
        "type": "bool",
        "game_default": "1",
        "description": "Forces your team to use the same model as you.",
        "label": "Force Model"
    },
    "cg_enemyModel": {
        "value": None,
        "type": "string",
        "game_default": "keel/pm",
        "description": "Displays enemy players with this model.",
        "label": "Enemy Model"
    },
    "cg_forceColors": {
        "value": None,
        "type": "bool",
        "game_default": "1",
        "description": "Displays teammate models with your own colors.",
        "label": "Force Colors"
    },
    "cg_enemyColors": {
        "value": None,
        "type": "string",
        "game_default": "g2222",
        "description": "Enemy model colors (CHBLS).",
        "label": "Enemy Colors"
    },
    "cg_forceTeamModel": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Enables the use of cg_teamModel for teammates.",
        "label": "Force Team Model"
    },
    "cg_teamModel": {
        "value": None,
        "type": "string",
        "game_default": "sarge/pm",
        "description": "Displays teammates with this model.",
        "label": "Team Model"
    },
    "cg_forceTeamColors": {
        "value": None,
        "type": "bitmask",
        "game_default": "15",
        "description": "Enables cg_redTeamColors/blueTeamColors.",
        "label": "Force Team Colors"
    },
    "cg_redTeamColors": {
        "value": None,
        "type": "string",
        "game_default": "cccab",
        "description": "Red team model colors.",
        "label": "Red Team Colors"
    },
    "cg_blueTeamColors": {
        "value": None,
        "type": "string",
        "game_default": "mmmpo",
        "description": "Blue team model colors.",
        "label": "Blue Team Colors"
    }
}

# --- 6. WEAPON SETTINGS ---
WEAPON_SETTINGS = {
    "cg_drawBrightWeapons": {
        "value": None,
        "type": "bitmask",
        "game_default": "0",
        "description": "Enables fullbright weapons (1=Self, 2=Team, 4=Enemy, etc).",
        "label": "Draw Bright Weapons"
    },
    "cg_drawBrightSpawns": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Draws spawn points more visibly.",
        "label": "Draw Bright Spawns"
    },
    "cg_noAmmoChange": {
        "value": None,
        "type": "discrete",
        "options": ["0", "1", "2"],
        "game_default": "1",
        "description": "Behavior when out of ammo. 1=Switch, can select empty.",
        "label": "No Ammo Change"
    },
    "cg_autoswitch": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Auto-switch to the weapon you pick up.",
        "label": "Auto Switch"
    },
    "cg_ammoWarning": {
        "value": None,
        "type": "bool",
        "game_default": "1",
        "description": "Out-of-ammo click sound.",
        "label": "Ammo Warning"
    },
    "cg_fallKick": {
        "value": None,
        "type": "bool",
        "game_default": "1",
        "description": "Enables camera bounce after a fall.",
        "label": "Fall Kick"
    },
    "cg_viewAdjustments": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Toggle for all cg_run and cg_bob cvars.",
        "label": "View Adjustments"
    },
    "cg_zoomAnimatiomTime": {
        "value": None,
        "type": "int",
        "min": 0,
        "max": 500,
        "game_default": "150",
        "description": "Zoom in/out duration in ms.",
        "label": "Zoom Animation Time"
    },
    "cg_trueLightning": {
        "value": None,
        "type": "float",
        "min": -1.0,
        "max": 1.0,
        "game_default": "1",
        "description": "LG beam prediction. 0=Server, 1=Client. Negative hides beam.",
        "label": "True Lightning"
    },
    "cg_altLightning": {
        "value": None,
        "type": "string",
        "game_default": "233",
        "description": "LG beam style (3 chars: Self, Enemy, Team).",
        "label": "Alt Lightning"
    },
    "cg_altPlasma": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Enables the CPMA PG.",
        "label": "Alt Plasma"
    },
    "cg_simpleItems": {
        "value": None,
        "type": "bool",
        "game_default": "0",
        "description": "Shows items as sprites.",
        "label": "Simple Items"
    },
    "cg_shadows": {
        "value": None,
        "type": "bool",
        "game_default": "1",
        "description": "Player shadows (other players only).",
        "label": "Shadows"
    },
    "cg_itemFX": {
        "value": None,
        "type": "bitmask",
        "game_default": "7",
        "description": "Item effects. 1=Bob, 2=Rotate, 4=Scale.",
        "label": "Item FX"
    },
    "cg_railStyle": {
        "value": None,
        "type": "bitmask",
        "game_default": "3",
        "description": "Rail trail elements. 1=Core, 2=Spiral, 4=Rings.",
        "label": "Rail Style"
    },
    "cg_railTrailTime": {
        "value": None,
        "type": "int",
        "min": 0,
        "max": 10000,
        "game_default": "400",
        "description": "Rail trail visibility duration in ms.",
        "label": "Rail Trail Time"
    },
    "cg_railCoreWidth": {
        "value": None,
        "type": "int",
        "min": 0,
        "max": 200,
        "game_default": "2",
        "description": "Width of the rail core.",
        "label": "Rail Core Width"
    },
    "cg_railRingStep": {
        "value": None,
        "type": "int",
        "min": 0,
        "max": 200,
        "game_default": "32",
        "description": "Distance between the rail rings.",
        "label": "Rail Ring Step"
    },
    "cg_railRingWidth": {
        "value": None,
        "type": "int",
        "min": 0,
        "max": 200,
        "game_default": "8",
        "description": "Width of the rail rings.",
        "label": "Rail Ring Width"
    },
    "cg_gibs": {
        "value": None,
        "type": "bool",
        "game_default": "1",
        "description": "Enables the gibs and blood spatter effect.",
        "label": "Gibs"
    },
    "com_blood": {
        "value": None,
        "type": "discrete",
        "options": ["0", "1", "2"],
        "game_default": "0",
        "description": "Draws blood when players are hit. 0=Disabled, 1=Old, 2=New.",
        "label": "Blood"
    },
    "cg_smoke_SG": {
        "value": None,
        "type": "bool",
        "game_default": "1",
        "description": "Smoke on the shotgun blast.",
        "label": "Smoke SG"
    },
    "cg_smokeRadius_GL": {
        "value": None,
        "type": "float",
        "min": 0.0,
        "max": 32.0,
        "game_default": "6",
        "description": "Size of the smoke trail for grenades.",
        "label": "Smoke Radius GL"
    },
    "cg_smokeRadius_RL": {
        "value": None,
        "type": "float",
        "min": 0.0,
        "max": 32.0,
        "game_default": "4",
        "description": "Size of the smoke trail for rockets.",
        "label": "Smoke Radius RL"
    },
    "cg_lightningImpact": {
        "value": None,
        "type": "discrete",
        "options": ["0", "1", "2"],
        "game_default": "0",
        "description": "Draws impact mark/sparks for LG.",
        "label": "Lightning Impact"
    },
    "cg_muzzleFlash": {
        "value": None,
        "type": "bool",
        "game_default": "1",
        "description": "Draws a muzzle flash when your gun is firing.",
        "label": "Muzzle Flash"
    },
    "cg_drawGun": {
        "value": None,
        "type": "discrete",
        "options": ["0", "1", "2"],
        "game_default": "2",
        "description": "Gun display mode. 0=No gun, 1=Sway, 2=No sway.",
        "label": "Draw Gun"
    },
    "cg_gunOffset": {
        "value": None,
        "type": "string",
        "game_default": "5, 0, 0",
        "description": "Moves the gun along the x,y,z axis.",
        "label": "Gun Offset"
    }
}