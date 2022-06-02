function getData(){
    var youtube_url = document.getElementById("youtube-url").value;
    var text_ip = document.getElementById("text-ip").value;
    var size = document.getElementById("size").value;

    //fetches the data from the api
    fetch(`http://miniproject05.pythonanywhere.com/result?youtube-url=${youtube_url}&text-ip=${text_ip}&size=${size}`)
        .then(response => response.json())
        .then(data => {
            //display the data
            document.getElementById("summary_res").innerHTML = '<h4 style="font-weight: bold;margin-top: 18px;margin-right: 2px;margin-bottom: 2px;margin-left: 2px;">Summarized Output</h4>'+data.summary;
        });
        
    }

