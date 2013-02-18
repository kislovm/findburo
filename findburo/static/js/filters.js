window.customFilters = {};

customFilters.linebreaks = function(input) {
    if(!input) return '';
    var strings = input.split(/(\r\n){2,}/g); 
    result = ''; 
    for (var i=0;i < strings.length;i++){
    	if (strings[i] != '\r\n') result += ('<p>'+ strings[i].replace(/\n/g, '<br \\>') +'</p>') 
    }
    return result;
}