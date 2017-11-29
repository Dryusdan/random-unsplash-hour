<?php
	header("Content-type: image/png");
	$x = 640; //largeur de mon image en PIXELS uniquement !
	$y = 480; //hauteur de mon image en PIXELS uniquement !
	$image = imagecreatetruecolor($x,$y);
	#$file = '/data/twelve.png';
	#imagepng($image, $file);
	
	$img = file_get_contents('https://source.unsplash.com/collection/1053828/640x480');
	imagepng($image);
	imagedestroy($image); 