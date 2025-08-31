"""
CSS Loading utilities for Streamlit applications.

Provides function to load and inject CSS stylesheets into Streamlit apps.
"""

import streamlit as st
import os
from typing import Union, List


def load_css(file_paths: Union[str, List[str]]) -> None:
    """
    Load one or multiple CSS files for application styling.
    
    Args:
        file_paths: Single CSS file path or list of CSS file paths
        
    Examples:
        load_css("static/styles/themes.css")
        load_css([
            "static/styles/themes.css",
            "static/styles/components.css", 
            "static/styles/main.css"
        ])
    """
    # Convert single file to list
    if isinstance(file_paths, str):
        file_paths = [file_paths]
    
    for file_path in file_paths:
        if os.path.exists(file_path):
            with open(file_path, encoding='utf-8') as f:
                st.html(f'<style>{f.read()}</style>')
        else:
            st.warning(f"CSS file not found: {file_path}")