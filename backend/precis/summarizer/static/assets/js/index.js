function main(){
    
    //get form values
    var youtube_url = document.getElementById("youtube-url").value;
    var text_ip = document.getElementById("text-ip").value;
    var size = document.getElementById("size").value;
    
    //fetches the data from the api
    fetch(`/result?youtube-url=${youtube_url}&text-ip=${text_ip}&size=${size}`)
    .then(response => response.json())
    .then((data) => {
        //display the data
        alert(data.summary);
        document.getElementById("summaryRes").innerHTML = data.summary;
    });
}




var button = document.getElementById('btn');
button.addEventListener("click", main);