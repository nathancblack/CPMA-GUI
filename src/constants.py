# src/constants.py
# This file stores all the variable names (keys) and bind actions
# that the GUI will control, organized by tab.

# --- 1. CONTROLS Tab ---

# 'seta' variables that will be toggles or text boxes
CONTROLS_SETA_KEYS = [
    "in_minimize",
    "cl_run"
]

# 'bind' actions that will be mapped to keys
CONTROLS_BIND_ACTIONS = [
    # Weapons
    "weapon 1",
    "weapon 2",
    "weapon 3",
    "weapon 4",
    "weapon 5",
    "weapon 6",
    "weapon 7",
    "weapon 8",
    "weapon 9",
    # Movement
    "+forward",
    "+back",
    "+moveleft",
    "+moveright",
    "+movedown",
    "+moveup",
    "+speed",
    # Actions
    "+attack",
    "+zoom",
    "+button2",
    "weapprev",
    "weapnext",
    "say_team ^aDropped ^y#w for ^e#n;drop;weapnext",
    "say_team ^aDropped ^yFlag for ^e#n;drop flag",
    "say_team ^aDr^xo^app^xe^ad ^bammo ^z#w for ^e#n;drop ammo",
    "kill",
    # Chat
    "say_team ^iFree ^y#i",
    "say_team ^eTook ^y#p",
    "say_team ^5QUAD-QUAD-QUAD",
    "say_team ^4LOW LOW LOW",
    "say_team ^cMID MID MID",
    "say_team ^3HIGH HIGH HIGH",
    # System Actions
    "togglemenu",
    "toggleconsole",
    "toggle ch_drawwarmup",
    "+scores",
    "messagemode",
    "messagemode2",
    "con_echo ^AA^BB^CC^DD^EE^FF^GG^HH^II^JJ^KK^LL^MM^NN^OO^PP^QQ^RR^SS^TT^UU^VV^WW^XX^YY^ZZ^00^99^88^77^66^55^44^33^22^11",
    "vote yes;play sound/misc/menu2",
    "vote no;play sound/misc/menu3",
    "ready;play sound/misc/menu3",
    "notready;play sound/misc/menu4",
    "team f",
    "team r;con_echo ^1RED",
    "team b;con_echo ^4BLUE",
    "team s;con_echo ^9SPEC",
    "+wstats",
    "screenshotJPEG;play sound/misc/menu1"
]

# --- 2. MOUSE Tab ---

MOUSE_KEYS = [
    "in_mouse",
    "m_filter",
    "m_speed",
    "ui_sensitivity",
    "m_yaw",
    "m_pitch",
    "m_accel",
    "m_accelStyle",
    "m_accelOffset",
    "m_limit",
    "cl_drawMouseLag"
]

# --- 3. VIDEO & GRAPHICS Tab ---

VIDEO_KEYS = [
    "com_maxfps",
    "r_gamma",
    "r_intensity",
    "r_greyScale",
    "r_fullBright",
    "r_Brightness",
    "r_mapBrightness",
    "r_vertexLight",
    "r_dynamicLight",
    "r_lightmap",
    "r_fastSky",
    "r_noPortals",
    "r_flares",
    "r_ext_max_anisotropy",
    "r_textureMode",
    "r_picmip",
    "r_detailTextures",
    "r_roundImagesDown",
    "r_colorMipLevels",
    "r_teleporterFlash",
    "r_monitor",
    "r_fullScreen",
    "vid_ypos",
    "vid_xpos",
    "r_blitMode",
    "r_mode",
    "r_width",
    "r_height",
    "r_customAspect",
    "r_displayRefresh",
    "r_swapInterval",
    "r_msaa",
    "r_lodbias",
    "r_maxPolys",
    "r_maxPolyVerts",
    "r_subdivisions",
    "r_debugLight",
    "r_showImages",
    "r_inGameVideo",
    "r_uiFullScreen",
    "r_finish",
    "r_ignoreGLErrors"
]

# --- 4. AUDIO Tab ---

AUDIO_KEYS = [
    "s_initSound",
    "s_autoMute",
    "s_volume",
    "s_musicVolume",
    "s_ambient",
    "s_announcer",
    "cg_oldCTFSounds",
    "cg_noTeamChatBeep",
    "cg_noChatBeep",
    "cg_noTaunt",
    "cg_noHitBeep"
]

# --- 5. HUD & UI Tab ---

HUD_UI_KEYS = [
    "cg_drawCrosshair",
    "cg_crosshairX",
    "cg_crosshairY",
    "cg_crosshairSize",
    "cg_crosshairHealth",
    "ch_crosshairAlpha",
    "ch_crosshairColor",
    "ch_crosshairHitColor",
    "ch_crosshairText",
    "ch_crosshairPulse",
    "ch_file",
    "ch_drawKeys",
    "cg_drawFriend",
    "cg_drawCrosshairNames",
    "ch_shortNames",
    "cg_drawRewards",
    "cg_draw2d",
    "cg_draw3dicons",
    "cg_damageDraw",
    "cl_noPrint",
    "con_noPrint",
    "con_drawHelp",
    "con_history",
    "con_scale",
    "con_notifyTime",
    "con_speed",
    "con_completionStyle",
    "ch_consoleLines",
    "con_colBG",
    "con_colBorder",
    "con_colArrow",
    "con_colShadow",
    "con_colHL",
    "con_colText",
    "con_colCVar",
    "con_colCmd",
    "con_colValue",
    "con_colHelp"
]

# --- 6. PLAYER & WEAPON Tab ---

PLAYER_WEAPON_KEYS = [
    "name",
    "nick",
    "cg_fov",
    "cg_zoomfov",
    "cg_drawGun",
    "cg_gunOffset",
    "color",
    "model",
    "cg_showPlayerLean",
    "cg_forceModel",
    "cg_enemyModel",
    "cg_forceColors",
    "cg_enemyColors",
    "cg_forceTeamModel",
    "cg_teamModel",
    "cg_forceTeamColors",
    "cg_redTeamColors",
    "cg_blueTeamColors",
    "cg_drawBrightWeapons",
    "cg_drawBrightSpawns",
    "cg_deadBodyDarken",
    "cg_noAmmoChange",
    "cg_autoSwitch",
    "cg_ammoWarning",
    "cg_fallKick",
    "cg_viewAdjustments",
    "cg_viewSize",
    "cg_zoomAnimationTime",
    "cg_trueLightning",
    "cg_altLightning",
    "cg_altPlasma",
    "cg_simpleItems",
    "cg_shadows",
    "cg_nomip",
    "cg_itemFX",
    "cg_railStyle",
    "cg_railTrailTime",
    "cg_railCoreWidth",
    "cg_railRingStep",
    "cg_railRingWidth",
    "cg_gibs",
    "com_blood",
    "cg_smoke_SG",
    "cg_smokeRadius_GL",
    "cg_smokeRadius_RL",
    "cg_lightningImpact",
    "cg_brassTime",
    "cg_marks",
    "cg_noProjectileTrail",
    "cg_muzzleFlash",
    "cg_stereoSeparation"
]