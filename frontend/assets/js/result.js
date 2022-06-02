function main(){
    var sURL = window.document.URL.toString();
    var url = new URL(sURL);

    var size = url.searchParams.get("size");
    var text_ip = url.searchParams.get("text-ip");
    var youtube_url = url.searchParams.get("youtube-url");
    
    fetch(`http://miniproject05.pythonanywhere.com/result?youtube-url=${youtube_url}&text-ip=${text_ip}&size=${size}`)
        .then(response => response.json())
        .then((data) => {
            //display the data
            document.getElementById("summaryRes").innerHTML = data.summary;
        });
    }
console.log('result.js loaded');
var summary = sessionStorage.getItem('summary');
document.getElementById("summaryRes").innerHTML = summary;