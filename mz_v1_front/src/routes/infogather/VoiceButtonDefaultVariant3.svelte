<script>
  import { createEventDispatcher } from 'svelte';
  
  const dispatch = createEventDispatcher();
  export let variant = 'variant-3';
  let className = '';
  export { className as class };
  export let style;
  const variantsClassName = 'default-' + variant;
  
  let mediaRecorder;
  let audioChunks = [];
  let isRecordingComplete = false; // 녹음 상태를 추적하는 변수
  let progress = 0;

  async function startRecording() {
    audioChunks = []; // 이전 녹음 데이터 초기화
    isRecordingComplete = false; // 녹음 시작 시, 녹음 완료 상태를 false로 설정

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorder = new MediaRecorder(stream);
      
      mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data);
      };
      
      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        const audioUrl = URL.createObjectURL(audioBlob);
        // 이벤트를 통해 오디오 URL을 부모 컴포넌트로 전달
        dispatch('audioRecorded', audioUrl );
        dispatch('blobUpdated', audioBlob);
        isRecordingComplete = true;
      };

      setTimeout(() => {
        mediaRecorder.start();
        progress = 100;
        dispatch('progressUpdated', progress);

        setTimeout(() => {
          mediaRecorder.stop();
        }, 15100); // 15초 후에 녹음을 멈춥니다.
      }, 3000); // 녹음 시작 전 3초 대기
      
    } catch (err) {
      console.error('오디오 입력을 시작하는데 실패했습니다:', err);
    }
  }

  // 녹음을 다시 시작하는 함수
  function restartRecording() {
    audioChunks = []; // 이전 녹음 데이터 초기화
    isRecordingComplete = false; // 다시 녹음할 준비가 되었으므로 false로 설정
    dispatch('audioRecorded', "");
    dispatch('progressUpdated',0);
  }
</script>

<div style="{'width: 100px; height: 50px; position: relative; ' + style}">
  {#if !isRecordingComplete}
    <!-- 녹음이 완료되지 않았을 때 audio record 이미지를 표시 -->
    <img
      class="{'frame-6 ' + className + ' ' + variantsClassName}"
      style="..."
      src="/join/frame-60.svg"
      on:click={startRecording}
      alt="audio record"
    />
  {:else}
    <!-- 녹음이 완료되었을 때 restart 이미지를 표시 -->
    <img
      class="{'frame-6 ' + className + ' ' + variantsClassName}"
      style="..."
      src="/join/restart.png"
      on:click={restartRecording}
      alt="restart"
    />
  {/if}
</div>
