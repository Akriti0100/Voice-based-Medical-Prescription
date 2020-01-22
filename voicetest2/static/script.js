'use strict'

let log = console.log.bind(console),
  id = val => document.getElementById(val),
  ul = id('ul'),
  gUMbtn = id('gUMbtn'),
  start = id('start'),
  stop = id('stop'),
  stream,
  recorder,
  counter=1,
  chunks,
  media;


gUMbtn.onclick = e => {
  let mv = id('mediaVideo'),
      mediaOptions = {
        video: {
          tag: 'video',
          type: 'video/webm',
          ext: '.mp4',
          gUM: {video: true, audio: true}
        },
        audio: {
          tag: 'audio',
          type: 'audio/wav',
          ext: '.wav',
          gUM: {audio: true}
        }
      };
  media = mv.checked ? mediaOptions.video : mediaOptions.audio;
  navigator.mediaDevices.getUserMedia(media.gUM).then(_stream => {
    stream = _stream;
    id('gUMArea').style.display = 'none';
    id('btns').style.display = 'inherit';
    start.removeAttribute('disabled');
    recorder = new MediaRecorder(stream);
    recorder.ondataavailable = e => {
      chunks.push(e.data);
      if(recorder.state == 'inactive')  makeLink();
    };
    log('got media successfully');
  }).catch(log);
}

start.onclick = e => {
  start.disabled = true;
  stop.removeAttribute('disabled');
  chunks=[];
  recorder.start();
}


stop.onclick = e => {
  stop.disabled = true;
  recorder.stop();
  start.removeAttribute('disabled');
}



function makeLink(){
  let blob = new Blob(chunks, {type: media.type })
    , url = URL.createObjectURL(blob)
    , li = document.createElement('li')
    , mt = document.createElement(media.tag)
    , hf = document.createElement('a')
  ;
  upload(blob);
  mt.controls = true;
  mt.src = url;
  hf.href = url;
  hf.download = `${counter++}${media.ext}`;
  hf.innerHTML = `donwload ${hf.download}`;
  li.appendChild(mt);
  li.appendChild(hf);
  ul.appendChild(li);
}
function upload(blob) {
            var formData = new FormData();
            formData.append("blob", blob, 'myfile');
            var xhr = new XMLHttpRequest();
            xhr.open('POST', "{% url 'record:upload' %}", true);
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
            xhr.setRequestHeader("PromptID", String(promptID).split("_")[0]);
            xhr.setRequestHeader("length", recordingTime);

            // progressBar = document.getElementById('progress');
            // progressBar.value = 0;
            // $('#progress').show();
            //
            // // Visualize upload progress
            // xhr.upload.onprogress = function (e) {
            //     if (e.lengthComputable) {
            //         progressBar.value = (e.loaded / e.total) * 100;
            //         progressBar.textContent = progressBar.value; // Fallback for unsupported browsers.
            //     }
            // };

            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {

                        writeMessages($.parseJSON(xhr.response));
                } else if (xhr.readyState == 4 && xhr.status == 400 || xhr.readyState == 4 && xhr.status == 500) {
                    alert("Error while Uploading - The admins have been notified. Please try again later")
                }
            };
            xhr.send(formData);
        }
