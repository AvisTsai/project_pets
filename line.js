var firebase;
$(function(){
  var $name = $('#name'),
      $content = $('#content'),
      $btn = $('#btn'),
      $show = $('#show');
  var config = {
    databaseURL: "https://ironman2017-27ae3.firebaseio.com/"
  };
  firebase.initializeApp(config);
  var database = firebase.database().ref();
  
  $btn.on('click',function(){
    var postData = {
      name:$('#name').val(),
      content:$('#content').val()
    };
    database.push(postData);
  });
  
  database.on('value', function(snapshot) {
    $show.html('');
    var arr = [];
    for(var i in snapshot.val()){
       arr.push(snapshot.val()[i]);
       $show.append('<span>'+snapshot.val()[i].name+' 說：'+snapshot.val()[i].content+'</span><br/>');
    }
  });
  
  
});