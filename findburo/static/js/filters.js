window.customFilters = {};

customFilters.linebreaks = function(input) {
    if(!input) return ''
    var strings = input.split('\n\n'); 
    result = ''; 
    for (var i=0;i < strings.length;i++){
        result += ('<p>'+ strings[i] +'</p>'.replace('\n', '<br \>')) 
    }
    return result;
}