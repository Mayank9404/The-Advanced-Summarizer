async function fetchData(url) {

    var size = 50;
    var text_ip = "";
    var youtube_url = url;

    const res=await fetch (` https://miniproject-b05.herokuapp.com/result/?youtube-url=${youtube_url}&text-ip=${text_ip}&size=${size}`);
    const record=await res.json();
    document.getElementById("summary_res").innerHTML=record.summary;
}
chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let url = tabs[0].url;
    fetchData(url)
});