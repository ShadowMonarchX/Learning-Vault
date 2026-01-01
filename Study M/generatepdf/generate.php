<?php 

if ($_SERVER['REQUEST_METHOD'] != 'POST') {
     exit;
}

define('ACCESSCHECK', TRUE);

require_once 'vendor/autoload.php';

use Classes\GeneratePDF;


$data = [
      'first_name' => $_POST['fname'] .' ' . $_POST['lname'],
      'last_name' => $_POST['email'],
      'hobby' => 'reading',
      'enquiry_field' => $_POST['enquiry']
];

$data = [
      'first_name' => $_POST['fname'],
      'last_name' => $_POST['lname'],
      'gender' => $_POST['gender'],
      'country'=> $_POST['country']
];

$pdf = new GeneratePdf;
$response = $pdf->generate($data);


header('Location: thanks.php?fname=' . $_POST['fname'] . '&link=' . $response);

