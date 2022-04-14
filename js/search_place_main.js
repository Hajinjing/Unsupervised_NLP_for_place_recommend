$('#search-icon').on('click', function(){
  $.get('../output/recommendation.json')
  .done(function(data){
    console.log(data.title["3939"]);
    if ($('#disabledTextInput').val() == data.title["3939"]){
      location.href='../html/search_place_result.html';
    }else {
      location.href='../html/empty_place_result.html';
    }
  })
  .fail(function(){
    console.log('실패함');
  })
})