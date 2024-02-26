<script>
  export let variant = 'variant-3';
  let className = '';
  export { className as class }; export let style;const variantsClassName = 'default-' + variant
  
  let mediaRecorder;
  let audioChunks = [];


  async function startRecording() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorder = new MediaRecorder(stream);
      
      mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data);
      };
      
      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        const audioUrl = URL.createObjectURL(audioBlob);
        const audio = new Audio(audioUrl);
        console.log(audioUrl)
        audio.play();
      };

      mediaRecorder.start();
      
      setTimeout(() => {
        mediaRecorder.stop();
      }, 6000); // 6초 후에 녹음을 멈춥니다.
    } catch (err) {
      console.error('오디오 입력을 시작하는데 실패했습니다:', err);
    }
  }

</script>
<div style="{'width: 50px; height: 50px; position: relative; ' + style}">
  <img
    class="{'frame-6 ' + className + ' ' + variantsClassName}"
    style="
      display: flex;
      flex-direction: row;
      gap: 10px;
      align-items: flex-start;
      justify-content: flex-start;
      height: auto;
      position: absolute;
      left: calc(50% - 25px);
      bottom: 0%;
      top: 0%;
      height: 100%;
      overflow: visible;
    "
    
    src="/join/frame-60.svg"
    on:click={startRecording}
    alt="audio record"
  />
</div>
