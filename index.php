<!DOCTYPE html>
<html lang="hu">
<head>
<title>Tiszatáj szakdolgozat</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<link rel="stylesheet" href="style.css?ver=<?php echo filemtime('style.css');?>">
    <link rel="icon"
          type="image/png"
          href="favicon.png">
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body style="padding-bottom:60px;">
<div class="jumbotron text-center" style="margin-bottom:0;padding-bottom:3%;">
  <h1>A Tiszatáj folyóirat archívuma</h1>
  <h3>Morfológiai elemzések</h3>
</div>

<nav class="navbar navbar-expand-lg navbar-light justify-content-center sticky-top" style="background-color: #e3f2fd;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse justify-content-center" id="navbarTogglerDemo03">
    <ul class="nav nav-pills nav-fill">
      <li class="nav-item active">
        <a class="nav-link" href="index.php">Útmutató<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="index.php?page=tiszataj">A Tiszatájról</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="index.php?page=list_creators">Szerző választása</a>
      </li>
        <li class="nav-item">
            <a class="nav-link" href="http://tiszataj.bibl.u-szeged.hu">A Tiszatáj archívuma</a>
        </li>
    </ul>
  </div>
</nav>

<div class="container" style="margin-top:30px">
  <div class="row">
    <div class="col">
<?php


if(isset($_GET["page"]) && $_GET["page"]!="") {
	$page = $_GET["page"];
	if(file_exists("".$page.".php")) {
		include_once ("".$page.".php");
	} else {
		include_once ("404.php");
	}
} else {
	include_once("main.php");
}


	 ?>
    </div>
  </div>
</div>

<footer class="fixed-bottom">
<div class="jumbotron text-center" style="margin-bottom:0;padding:1%;height:60px;">
    <p>Készítette: Szűcs Nerina, "A Tiszatáj folyóirat archívumának morfológiai elemzése" c. szakdolgozat részeként © 2021</p>
</div>
</footer>
</body>
</html>