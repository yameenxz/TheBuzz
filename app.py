<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

body {
    margin: 0;
    background: url("https://res.cloudinary.com/dnne6eiae/image/upload/v1776867977/roy69_b8ljl4.jpg") no-repeat center center fixed;
    background-size: cover;
    font-family: sans-serif;
}

/* HEADER */
.header {
    text-align: center;
    margin: 0;
    padding: 0;
}

/* 🔥 BIGGER LOGO */
.header img {
    width: 260px;   /* 👈 increased from 180px */
    display: block;
    margin: 0 auto;
}

/* VIDEO */
.video-section {
    position: relative;
    width: 92%;
    height: 80vh;
    margin: -40px auto 0 auto;
    overflow: hidden;
    border-radius: 12px;
}

.video-section video {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.video-section::after {
    content: "";
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.25);
    z-index: 1;
}

/* BUTTON */
.btn {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    padding: 15px 40px;
    font-size: 20px;
    background: white;
    color: black;
    border-radius: 10px;
    text-decoration: none;
    z-index: 2;
}

.btn:hover {
    transform: translate(-50%, -50%) scale(1.05);
    background: #f0f0f0;
}

</style>
</head>

<body>

<div class="header">
    <img src="https://res.cloudinary.com/dnne6eiae/image/upload/q_auto,f_auto/1000055489-Photoroom_cymvnr.png">
</div>

<div class="video-section">
    <video autoplay muted loop playsinline>
        <source src="https://res.cloudinary.com/dnne6eiae/video/upload/q_auto,f_auto/roy123_yizolb.mp4" type="video/mp4">
    </video>

    <a href="https://the-buzz-btdh.vercel.app/" target="_blank" class="btn">
        Register Now
    </a>
</div>

</body>
</html>
