<?php
require "choose_creator.php";
$arg = $_GET["title"];
putenv("PYTHONIOENCODING=utf-8");
$output = shell_exec('python "./scripts/pos_analysis.py" "'.$arg.'" 2>&1');
$formatted_output = ltrim($output, 0);
$decodedJson = json_decode($formatted_output);
echo '<h1 class="ctitle">' .$decodedJson[0]. ' - ' . $decodedJson[1] . '</h1>';
echo '<div style="margin-left:20%;margin-right:20%;">';
echo '<div class="card"><div class="card-body">Szavak száma: '.$decodedJson[2].'</div></div>';
echo '<div class="card"><div class="card-body">Leggyakrabban használt szó: '.$decodedJson[16].'</div></div>';
echo '</div>';
echo '<div style="margin-left:5%;margin-right:5%;">';
echo '<div class="card text-white bg-primary mb-3" style="width: 14rem;"><div class="card-header" style="text-align:center;">Főnevek száma</div>
  <div class="card-body">
    <h5 class="card-title" style="text-align:center;">'.$decodedJson[3].'</h5>
  </div>
</div>';
echo '<div class="card text-white bg-info mb-3" style="width: 14rem;"><div class="card-header" style="text-align:center;">Igék száma</div>
  <div class="card-body">
    <h5 class="card-title" style="text-align:center;">'.$decodedJson[4].'</h5>
  </div>
</div>';
echo '<div class="card text-white bg-info mb-3 harom" style="width: 14rem;"><div class="card-header" style="text-align:center;">Melléknevek száma</div>
  <div class="card-body">
    <h5 class="card-title" style="text-align:center;">'.$decodedJson[5].'</h5>
  </div>
</div>';
echo '</div>';
    echo '<div class="card bg-light mb-3" style="width: 10rem;"><div class="card-header" style="text-align:center;height:50px;">Határozószók</div>
  <div class="card-body">
    <h5 class="card-title" style="text-align:center;">'.$decodedJson[6].'</h5>
  </div>
</div>';
echo '<div class="card bg-light mb-3" style="width: 10rem;"><div class="card-header" style="text-align:center;height:50px;">Tulajdonnevek</div>
  <div class="card-body">
    <h5 class="card-title" style="text-align:center;">'.$decodedJson[7].'</h5>
  </div>
</div>';
echo '<div class="card bg-light mb-3" style="width: 10rem;"><div class="card-header" style="text-align:center;height:50px;">Indulatszavak</div>
  <div class="card-body">
    <h5 class="card-title" style="text-align:center;">'.$decodedJson[8].'</h5>
  </div>
</div>';
echo '<div class="card bg-light mb-3" style="width: 10rem;"><div class="card-header" style="text-align:center;height:50px;">Névmások</div>
  <div class="card-body">
    <h5 class="card-title" style="text-align:center;">'.$decodedJson[9].'</h5>
  </div>
</div>';
echo '<div class="card bg-light mb-3" style="width: 10rem;"><div class="card-header" style="text-align:center;height:50px;">Determinánsok</div>
  <div class="card-body">
    <h5 class="card-title" style="text-align:center;">'.$decodedJson[10].'</h5>
  </div>
</div>';
echo '<div class="card bg-light mb-3" style="width: 10rem;"><div class="card-header" style="text-align:center;font-size:85%;height:50px;">Elöljárók/névutók</div>
  <div class="card-body">
    <h5 class="card-title" style="text-align:center;">'.$decodedJson[11].'</h5>
  </div>
</div>';
echo '<div class="card bg-light mb-3" style="width: 10rem;"><div class="card-header" style="text-align:center;height:50px;">Segédigék</div>
  <div class="card-body">
    <h5 class="card-title" style="text-align:center;">'.$decodedJson[12].'</h5>
  </div>
</div>';
echo '<div class="card bg-light mb-3" style="width: 10rem;"><div class="card-header" style="text-align:center;height:50px;">Kötőszavak</div>
  <div class="card-body">
    <h5 class="card-title" style="text-align:center;">'.$decodedJson[13].'</h5>
  </div>
</div>';
echo '<br><br><br>';
echo '<h1 class="ctitle">Szógyakorisági táblázat</h1>';
echo '<div class="row"><div class="column">';
echo '<table class="table wordfreq"><thead class="thead-dark"><tr><th>Szó</th><th>Gyakoriság</th></tr></thead>';
echo '<tr><td>'. $decodedJson[17]. '</td>';
echo  '<td>' . $decodedJson[18] . '</td></tr>';
echo '<tr><td>'. $decodedJson[19]. '</td>';
echo  '<td>' . $decodedJson[20] . '</td></tr>';
echo '<tr><td>'. $decodedJson[21]. '</td>';
echo  '<td>' . $decodedJson[22] . '</td></tr>';
echo '<tr><td>'. $decodedJson[23]. '</td>';
echo  '<td>' . $decodedJson[24] . '</td></tr>';
echo '<tr><td>'. $decodedJson[25]. '</td>';
echo  '<td>' . $decodedJson[26] . '</td></tr>';
echo '<tr><td>'. $decodedJson[27]. '</td>';
echo  '<td>' . $decodedJson[28] . '</td></tr>';
echo '<tr><td>'. $decodedJson[29]. '</td>';
echo  '<td>' . $decodedJson[30] . '</td></tr>';
echo '<tr><td>'. $decodedJson[31]. '</td>';
echo  '<td>' . $decodedJson[32] . '</td></tr>';
echo '<tr><td>'. $decodedJson[33]. '</td>';
echo  '<td>' . $decodedJson[34] . '</td></tr>';
echo '<tr><td>'. $decodedJson[35]. '</td>';
echo  '<td>' . $decodedJson[36] . '</td></tr>';
echo '</table>';
echo '</div>';
echo '<div class="column">';
echo '<table class="table wordfreq"><thead class="thead-dark"><tr><th>Szó</th><th>Gyakoriság</th></tr></thead>';
echo '<tr><td>'. $decodedJson[37]. '</td>';
echo  '<td>' . $decodedJson[38] . '</td></tr>';
echo '<tr><td>'. $decodedJson[39]. '</td>';
echo  '<td>' . $decodedJson[40] . '</td></tr>';
echo '<tr><td>'. $decodedJson[41]. '</td>';
echo  '<td>' . $decodedJson[42] . '</td></tr>';
echo '<tr><td>'. $decodedJson[37]. '</td>';
echo  '<td>' . $decodedJson[38] . '</td></tr>';
echo '<tr><td>'. $decodedJson[39]. '</td>';
echo  '<td>' . $decodedJson[40] . '</td></tr>';
echo '<tr><td>'. $decodedJson[41]. '</td>';
echo  '<td>' . $decodedJson[42] . '</td></tr>';
echo '<tr><td>'. $decodedJson[43]. '</td>';
echo  '<td>' . $decodedJson[44] . '</td></tr>';
echo '<tr><td>'. $decodedJson[45]. '</td>';
echo  '<td>' . $decodedJson[46] . '</td></tr>';
echo '<tr><td>'. $decodedJson[47]. '</td>';
echo  '<td>' . $decodedJson[48] . '</td></tr>';
echo '<tr><td>'. $decodedJson[49]. '</td>';
echo  '<td>' . $decodedJson[50] . '</td></tr>';
echo '</table>';
echo '</div></div>';