$.get('../output/recommendation.json')
.done((data) => {  
    var key_list = Object.keys(data.title);
    // console.log(key_list);
    for (var i in key_list) {
        var template = `
        <div class="row col-md-6 mt-2 mb-2 items">
          <div class="col-md-6 flex-shrink-0">
            <h5>`+ data.title[key_list[i]] +`</h5>
            <img src="../image/parkimg.jpeg" alt="...">
          </div>
          <div class="row col-md-6 flex-grow-1">
            <div class="col-md-6 cherry item">자전거</div>
            <div class="col-md-6 cherry item">갯벌</div>
            <div class="col-md-6 cherry item">생태공원</div>
            <div class="col-md-6 cherry item">갯벌</div>
            <div class="col-md-6 cherry item">체험교육</div>
            <div class="col-md-6 cherry item">갯벌</div>
            <div class="col-md-6 cherry item">갯벌</div>
            <div class="col-md-6 cherry item">자전거</div>
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
  console.log(idx);
  if (idx == 10){
    $('.plus').fadeIn();
    $('.plus').removeAttr('style');
    $('.plus').hide();
  }
  
  for (var j=idx; j<(idx+2); j++){
    $('.items').eq(j).fadeIn();
    $('.items').eq(j).removeAttr('style');
    $('.items').eq(j).removeClass('items-hide');
  }
  idx += 2;
})
