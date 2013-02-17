window.customFilters = {};

customFilters.linebreaks = function(input) {
    if(!input) return ''
    var strings = input.split(/\n{2,}/); 
    result = ''; 
    for (var i=0;i < strings.length;i++){
        result += ('<p>'+ strings[i].replace('\n', '<br \\>') +'</p>') 
    }
    return result;
}