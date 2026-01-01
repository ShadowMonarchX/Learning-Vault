<?php
namespace Classes;

if(!defined('ACCESSCHECK')) {
      die('Direct access not permitted');
}


use mikehaertl\pdftk\Pdf;

class GeneratePDF {
      public function generate($data)
      {      

            $filePath = 'C:\xampp\htdocs\generatepdf\blank.pdf';
            $fullPath = realpath($filePath);

            try {
            if (!$fullPath) {
                  throw new Exception("File not found: $filePath");
            }

            $filename = 'pdf_' . rand(2000,1200000) . '.pdf';

            $pdf = new Pdf($fullPath, ['useExec' => true, 'command' => 'C:\\Program Files (x86)\\PDFtk\\bin\\pdftk.exe']);
            ob_clean();
            $pdf->fillForm($data);
            $pdf->send('output.pdf');
            if ($pdf->getError()) {
                  // Handle error, e.g., log it or show a message to the user
                  echo 'Error: ' . $pdf->getError();
                  exit; // Exit the script
            }

            return $filename;
            } catch (Exception $e) {
            // Handle any other exceptions that might occur
            echo 'Exception: ' . $e->getMessage();
            exit;
            }


      }
}