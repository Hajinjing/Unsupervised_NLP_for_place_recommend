$.get('../output/recommendation.json')
.done((data) => {  
    var key_list = Object.keys(data.title);
    // console.log(key_list);
    for (var i in key_list) {
        var template = `
        <div class="row col-md-6 mt-2 mb-2 items">
          <div class="col-md-6 flex-shrink-0">
            <a class="item-title" href="../html/place_content.html">`+ data.title[key_list[i]] +`</a>
            <a href="../html/place_content.html">
              <img src="../image/parkimg.jpeg" alt="...">
            </a>
          </div>
          <div class="row col-md-6 flex-grow-1 justify-content-center text-center">
            <div class="col-md-6 cherry1 item p-1"><span class="align-text-top">자전거</span></div>
            <div class="col-md-6 cherry1 item p-1"><span class="align-text-top">갯벌</span></div>
            <div class="col-md-6 cherry1 item p-1"><span class="align-text-top">생태공원</span></div>
            <div class="col-md-6 cherry1 item p-1"><span class="align-text-top">갯벌</span></div>
            <div class="col-md-6 cherry1 item p-1"><span class="align-text-top">체험교육</span></div>
            <div class="col-md-6 cherry1 item p-1"><span class="align-text-top">갯벌</span></div>
            <div class="col-md-6 cherry1 item p-1"><span class="align-text-top">갯벌</span></div>
            <div class="col-md-6 cherry1 item p-1"><span class="align-text-top">자전거</span></div>
          </div>
        </div>`;
        if (i >= 4) {
          $('.d-flex').eq(1).append(template);
          $('.items').eq(i).addClass('items-hide');
        }else {
          $('.items').eq(i).removeClass('items-hide');  
          $('.d-flex').eq(1).append(template);
        }
    }
})
.fail(function(){
  console.log('실패함');
})

let idx = 4;
$('.plus').on('click',function(){
  // console.log($('.items').eq(idx));
  
  for (var j=idx; j<(idx+2); j++){
    $('.items').eq(j).fadeIn();
    $('.items').eq(j).removeAttr('style');
    $('.items').eq(j).removeClass('items-hide');
    if ($('.items').eq(-1)){
      $('.plus').fadeIn();
      $('.plus').removeAttr('style');
      $('.plus').hide();
    }else {
      continue;
    }
  }
  idx += 2;
})
$('div i').on('click',function(){
  location.href="../html/search_place_main.html";
})
$('img').on('click',function(){
  location.href="../html/place_content.html";
})
