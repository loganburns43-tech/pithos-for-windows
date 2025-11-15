# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: nil; -*-
"""Helpers for applying the optional dark theme."""

import gtk

_DARK_THEME_RC = """
style "pithos-dark" {
    bg[NORMAL]      = "#232629"
    bg[PRELIGHT]    = "#34393d"
    bg[ACTIVE]      = "#2f3438"
    bg[SELECTED]    = "#3d444b"
    bg[INSENSITIVE] = "#232629"

    fg[NORMAL]      = "#f0f0f0"
    fg[PRELIGHT]    = "#ffffff"
    fg[ACTIVE]      = "#ffffff"
    fg[SELECTED]    = "#ffffff"
    fg[INSENSITIVE] = "#8a8d90"

    text[NORMAL]      = "#f5f5f5"
    text[PRELIGHT]    = "#ffffff"
    text[ACTIVE]      = "#ffffff"
    text[SELECTED]    = "#ffffff"
    text[INSENSITIVE] = "#8a8d90"

    base[NORMAL]      = "#1b1e21"
    base[PRELIGHT]    = "#2a2e31"
    base[ACTIVE]      = "#2a2e31"
    base[SELECTED]    = "#3d444b"
    base[INSENSITIVE] = "#1b1e21"

    engine "clearlooks" {
        reliefstyle = 2
        radius = 3.5
    }
}

widget "*PithosDark*" style "pithos-dark"
"""

gtk.rc_parse_string(_DARK_THEME_RC)


def _set_widget_name(widget, enabled):
    original_name = widget.get_data('pithos-original-widget-name')
    if original_name is None:
        original_name = widget.get_name()
        widget.set_data('pithos-original-widget-name', original_name)

    if enabled:
        widget.set_name('PithosDark')
    else:
        widget.set_name(original_name)

    if isinstance(widget, gtk.Container):
        for child in widget.get_children():
            _set_widget_name(child, enabled)


def apply_dark_theme_to_widget(widget, enabled):
    """Apply or remove the dark theme from a widget tree."""
    if not isinstance(widget, gtk.Widget):
        return

    _set_widget_name(widget, enabled)
    settings = widget.get_settings()
    if settings is not None:
        gtk.rc_reset_styles(settings)


def apply_dark_theme_to_builder(builder, enabled):
    """Apply or remove the dark theme to all widgets inside a builder."""
    if builder is None:
        return

    for obj in builder.get_objects():
        if isinstance(obj, gtk.Widget):
            _set_widget_name(obj, enabled)
            settings = obj.get_settings()
            if settings is not None:
                gtk.rc_reset_styles(settings)
