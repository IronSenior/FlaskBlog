

function showReplyForm(commentid) {
    var formid = "form-" + commentid
    
    if (document.getElementById(formid).style.display === "none") {
      document.getElementById(formid).style.display = "block";
    } else {
      document.getElementById(formid).style.display = "none";
    } 
}