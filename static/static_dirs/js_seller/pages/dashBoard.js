/**
 * Created by ashishagrawal on 15/08/15.
 */
    $(function(){
    $("#target").attr("onclick","confirmDel(id); return false;")
})

function confirmDel() {
    //$("#deleteModal").modal();
    alert("id passed is: "+ $(this).attr(id));
}