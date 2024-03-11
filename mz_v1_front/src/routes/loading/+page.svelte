<script>
    import ButtonStyleOutlined from "../join/ButtonStyleOutlined.svelte";
    import HeaderLogin from "../../components/header/header_login.svelte";
    import PlaceholderImage from "../join/PlaceholderImage.svelte";
    let className = "";
    export { className as class };
    export let style;
  </script>
  <div
    style="{'background: var(--neutral-0, #ffffff); display: flex; flex-direction: column; gap: 160px; align-items: center; justify-content: flex-start; height: 845px; position: relative; ' + style}"
  >
   <HeaderLogin />
    <div
      style="
        display: flex;
        flex-direction: row;
        gap: 82px;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        width: 1103px;
        height: 429px;
        position: relative;
      "
    >
      <div
        style="
          display: flex;
          flex-direction: row;
          gap: 82px;
          align-items: center;
          justify-content: flex-start;
          flex-shrink: 0;
          height: 423px;
          position: relative;
        "
      >
        <div
          style="
            display: flex;
            flex-direction: row;
            gap: 82px;
            align-items: center;
            justify-content: flex-start;
            flex-shrink: 0;
            height: 401px;
            position: relative;
          "
        >
          <div
            style="
              background: #ffffff;
              border-radius: 10px;
              border-style: solid;
              border-color: #878787;
              border-width: 0.5px;
              padding: 47px 0px 47px 0px;
              display: flex;
              flex-direction: row;
              gap: 10px;
              align-items: flex-start;
              justify-content: flex-start;
              flex-shrink: 0;
              width: 451px;
              height: 395px;
              position: relative;
              box-shadow: 0px 4px 64px 0px rgba(0, 0, 0, 0.05);
              overflow: hidden;
            "
          >
            <div
              style="
                display: flex;
                flex-direction: column;
                gap: 20px;
                align-items: center;
                justify-content: center;
                flex-shrink: 0;
                height: 193px;
                position: relative;
              "
            >
              <div
                style="
                  display: flex;
                  flex-direction: column;
                  gap: 20px;
                  align-items: center;
                  justify-content: center;
                  flex-shrink: 0;
                  height: 294px;
                  position: relative;
                "
              >
                <div
                  style="
                    text-align: center;
                    position: relative;
                    width: 451px;
                    height: 30px;
                    font-size: 16pt;
                  "
                >
                  <span>
                    <span class="div-2-span2"><br /></span>
                    <span class="div-2-span3">
                      생성 요청했습니다.
                      <br />
                      예상 소요시간은 ~분 입니다.
                    </span>
                  </span>
                </div>
              </div>
              <ButtonStyleOutlined
                style="
                  border-color: var(--7b95b7, #6b6b6b);
                  flex-shrink: 0;
                  height: 46px;
                "
                name="메인으로 돌아가기"
                targetPath="/home"
              ></ButtonStyleOutlined>
              <ButtonStyleOutlined
                style="
                  border-color: var(--7b95b7, #6b6b6b);
                  flex-shrink: 0;
                  height: 46px;
                "
                name="결과목록으로 가기"
                targetPath="/resultlist"
              ></ButtonStyleOutlined>
            </div>
          </div>
          <PlaceholderImage
            style="flex-shrink: 0; width: 405px; height: 405px"
            filename="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2VuaGd0ZzVtejhvbnQ5YTUzYmQ3ZGpqanQ2MWU2MG9uMWgyMjM0dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oEjI6SIIHBdRxXI40/giphy.gif"
          ></PlaceholderImage>
        </div>
      </div>
    </div>
  </div>