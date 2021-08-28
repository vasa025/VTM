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
        $fname = $_REQUEST['fname'];
        $lname =  $_REQUEST['lname'];
        $date = $_REQUEST['date'];
        $email = $_REQUEST['email'];
        $Ph_no = $_REQUEST['Ph_no'];
        $gender = $_REQUEST['gender'];
        $address = $_REQUEST['address'];
        
        
        $sql = "INSERT INTO vendor  VALUES ('$c_id','$fname','$lname','$date','$email','$Ph_no','$gender','$address')";

          
         
        if(mysqli_query($conn, $sql)){
            echo "<h3> vendor data stored in a database successfully </h3>"; 
  
           
        } else{
            echo "ERROR: Hush! Sorry $sql. " 
                . mysqli_error($conn);
        }
          
        
        mysqli_close($conn);
        ?>
  
</body>
  
</html>