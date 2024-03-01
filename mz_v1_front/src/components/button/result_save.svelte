<script>
    export let targetImage = "target_image_path.jpg";
    
    function downloadImage() {
    const a = document.createElement('a');
    a.href = targetImage;
    a.download = targetImage.split('/').pop(); // 원하는 파일 이름으로 변경하세요.
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  }
</script>

<img on:click={downloadImage}
              class="tabler-download2"
              style="
                flex-shrink: 0;
                width: 48px;
                height: 48px;
                position: relative;
                overflow: visible;
              "
              src="/join/tabler-download1.svg"
              alt="save"
            />