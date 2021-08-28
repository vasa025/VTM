<?php
  
$customer_id = $_REQUEST['customer_id'];
  
$con = mysqli_connect("localhost", "root", "", "project3");
  
if ($customer_id !== "") {
       
    $query = mysqli_query($con, "SELECT purchased_amt, 
    paid_amt,balance_amt FROM transaction WHERE customer_id='$customer_id'");
  
    $row = mysqli_fetch_array($query);
  
    $purchased_amt = $row["purchased_amt"];
  
    $paid_amt = $row["paid_amt"];

    $balance_amt = $row["balance_amt"];
}
  
$result = array("$purchased_amt", "$paid_amt","$balance_amt");
  
$myJSON = json_encode($result);
echo $myJSON;
?>

