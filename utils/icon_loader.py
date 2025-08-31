"""
SVG Icon Management for Streamlit Applications

Provides utilities for loading and customizing SVG icons in Streamlit dashboards.
Icons are expected to be stored in static/icons/ directory.
"""

import streamlit as st
import os
from typing import Optional

def load_icon_simple(icon_name: str, width: int = 24) -> None:
    """
    Display SVG icon using Streamlit's native image component.
    
    Args:
        icon_name: Icon filename without .svg extension
        width: Icon width in pixels
        
    Example:
        load_icon_simple("dashboard", width=32)
    """
    icon_path = f"static/icons/{icon_name}.svg"
    
    if os.path.exists(icon_path):
        st.image(icon_path, width=width)
    else:
        st.error(f"Icon '{icon_name}' not found")

def load_icon_advanced(icon_name: str, size: int = 24, color: str = "currentColor") -> str:
    """
    Load and customize SVG icon for inline usage.
    
    Args:
        icon_name: Icon filename without .svg extension
        size: Icon dimensions in pixels (width and height)
        color: Icon color (hex, rgb, or CSS color name)
        
    Returns:
        Customized SVG markup as string
        
    Example:
        st.markdown(f'### {load_icon_advanced("dashboard", 24, "#2563EB")} Dashboard', 
                   unsafe_allow_html=True)
    """
    icon_path = f"static/icons/{icon_name}.svg"
    
    if not os.path.exists(icon_path):
        return f'<span style="color: red;">Icon "{icon_name}" not found</span>'
    
    with open(icon_path, 'r', encoding='utf-8') as f:
        svg_content = f.read()
    
    # Apply customizations
    svg_content = svg_content.replace('width="24"', f'width="{size}"')
    svg_content = svg_content.replace('height="24"', f'height="{size}"')
    svg_content = svg_content.replace('stroke="currentColor"', f'stroke="{color}"')
    svg_content = svg_content.replace('fill="currentColor"', f'fill="{color}"')
    
    return svg_content