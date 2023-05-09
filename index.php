<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Calculator</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
  <link href="utils.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <h1 class="text-center">Welcome To Calculate</h1>
  <div class="container flex flex-col items-center mx-auto m-w-20">
    <div class="row">
      <input class="input" type="text" />
    </div>

    <hr style="width:25%">

    <div class="row">
      <button class="button" style="color: orangered;">C</button>
      <button class="button" style="color: orangered;">%</button>
      <button class="button" style="color: orangered;">M+</button>
      <button class="button" style="color: orangered;">M-</button>
    </div>
    <div class="row">
      <button class="button">7</button>
      <button class="button">8</button>
      <button class="button">9</button>
      <button class="button" style="color: orangered;">*</button>
    </div>
    <div class="row">
      <button class="button">4</button>
      <button class="button">5</button>
      <button class="button">6</button>
      <button class="button" style="color: orangered;">/</button>
    </div>
    <div class="row">
      <button class="button">1</button>
      <button class="button">2</button>
      <button class="button">3</button>
      <button class="button" style="color: orangered;">+</button>
    </div>
    <div class="row">
      <button class="button">.</button>
      <button class="button">0</button>
      <button class="button">-</button>
      <button class="button" style="color: whitesmoke; border-radius: 10% 30%; background-color: orangered;">=</button>
    </div>
  </div>
  <script src="script.js"></script>
</body>

</html>