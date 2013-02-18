window.customFilters = {};

customFilters.linebreaks = function(input) {
    if(!input) return '';
    var strings = input.split(/\r\n\r\n{1,}/); 
    result = ''; 
    for (var i=0;i < strings.length;i++){
        result += ('<p>'+ strings[i].replace(/\n/g, '<br \\>') +'</p>') 
    }
    return result;
}