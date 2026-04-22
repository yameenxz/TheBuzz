import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="THE BUZZ", layout="wide")

BG_IMAGE_URL = "https://res.cloudinary.com/dnne6eiae/image/upload/v1776867977/roy69_b8ljl4.jpg"

st.markdown(f"""
<style>
.stApp {{
    background: url("{BG_IMAGE_URL}") no-repeat center center fixed;
    background-size: cover;
}}

.block-container {{
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
}}
</style>
""", unsafe_allow_html=True)

VIDEO_URL = "https://res.cloudinary.com/dnne6eiae/video/upload/q_auto,f_auto/roy123_yizolb.mp4"

HEADER_URL = "https://res.cloudinary.com/dnne6eiae/image/upload/q_auto,f_auto/1000055489-Photoroom_cymvnr.png"

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>

body {{
    margin: 0;
}}

/* HEADER */
.header {{
    width: 100%;
    text-align: center;
    padding: 40px 0 6px 0;
}}

.header img {{
    width: 220px;
}}

/* VIDEO */
.hero {{
    position: relative;
    height: calc(100vh - 85px);
    margin-top: -40px;
    width: 100%;
    overflow: hidden;
}}

.hero video {{
    position: absolute;
    width: 100%;
    height: 100%;
    object-fit: cover;
}}

.hero::after {{
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0,0,0,0.25);
}}

.overlay {{
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
}}

.btn {{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    padding: 15px 40px;
    font-size: 20px;
    background: white;
    color: black;
    border: none;
    border-radius: 10px;
    cursor: pointer;
}}

.btn:hover {{
    transform: translate(-50%, -50%) scale(1.05);
    background: #f0f0f0;
}}

</style>
</head>

<body>

<div class="header">
    <img src="{HEADER_URL}">
</div>

<div class="hero">
    <video autoplay muted loop playsinline>
        <source src="{VIDEO_URL}" type="video/mp4">
    </video>

    <div class="overlay">

        <button class="btn" onclick="alert('Register coming soon')">
            Register Now
        </button>
    </div>
</div>

</body>
</html>
"""

components.html(html_code, height=1000)