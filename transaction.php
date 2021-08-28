<!DOCTYPE html>
<html>
  
<head>
    <title>Insert Page page</title>
</head>
  
<body>
    
        <?php
        $conn = mysqli_connect("localhost", "root", "", "project3");
          
        
        if($conn === false){
            die("ERROR: Could not connect. " 
                . mysqli_connect_error());
        }
          
        
        $c_id =  $_REQUEST['c_id'];
        $date = $_REQUEST['date'];
        $p_amt = $_REQUEST['p_amt'];
        $paid_amt =  $_REQUEST['paid_amt'];
        
        $sql = "INSERT INTO transaction  VALUES ('$c_id','$date','$p_amt','$paid_amt')";

          
         
        if(mysqli_query($conn, $sql)){
            header("location: transaction.html");  
                   
           
        } else{
            echo "ERROR: Hush! Sorry $sql. " 
                . mysqli_error($conn);
        }
          
        
        mysqli_close($conn);
        ?>
  
</body>
  
</html>