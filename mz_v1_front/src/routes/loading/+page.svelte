<script>
    import ButtonStyleFilled from "../join/ButtonStyleFilled.svelte";
    import ButtonStyleOutlined from "../join/ButtonStyleOutlined.svelte";
    import PlaceholderImage from "../join/PlaceholderImage.svelte";
    let className = "";
    export { className as class };
    export let style;
  </script>
  <div
    style="{'background: var(--neutral-0, #ffffff); display: flex; flex-direction: column; gap: 160px; align-items: center; justify-content: flex-start; height: 845px; position: relative; ' + style}"
  >
    <div
      style="
        background: var(--neutral-0, #ffffff);
        border-style: solid;
        border-color: var(--neutral-2, #dee5ed);
        border-width: 0px 0px 1px 0px;
        padding: 8px 98px 8px 98px;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        flex-shrink: 0;
        width: 1440px;
        height: 72px;
        position: relative;
        overflow: hidden;
      "
    >
      <div style="flex-shrink: 0; width: 299px; height: 55px; position: static">
        <div
          style="
            color: var(--7b95b7, #6b6b6b);
            text-align: left;
            font-family: 'TitanOne-Regular', sans-serif;
            font-size: 24px;
            line-height: 24px;
            font-weight: 400;
            position: absolute;
            right: 72.43%;
            left: 13.06%;
            width: 14.51%;
            bottom: 23.61%;
            top: 43.06%;
            height: 33.33%;
          "
        >
          Make Zenerator
        </div>
        <img
          class="{'image-2 ' + className}"
          style="
            position: absolute;
            right: 86.94%;
            left: 6.81%;
            width: 6.25%;
            bottom: 11.81%;
            top: 11.81%;
            height: 76.39%;
            object-fit: cover;
          "
          src="/join/image-20.png"
          alt="logo"
        />
      </div>
      <div
        style="
          display: flex;
          flex-direction: row;
          gap: 48px;
          align-items: center;
          justify-content: flex-start;
          flex-shrink: 0;
          position: relative;
        "
      >
        <a href="/aboutus_login"
          style="
            color: var(--7b95b7, #6b6b6b);
            text-align: center;
            font-family: var(
              --body-small-font-family,
              'DmSans-Regular',
              sans-serif
            );
            font-size: var(--body-small-font-size, 16px);
            line-height: var(--body-small-line-height, 24px);
            font-weight: var(--body-small-font-weight, 400);
            position: relative;
          "
        >
          About us
    </a>
        <a href="/"
          style="
            color: var(--7b95b7, #6b6b6b);
            text-align: center;
            font-family: var(
              --body-small-font-family,
              'DmSans-Regular',
              sans-serif
            );
            font-size: var(--body-small-font-size, 16px);
            line-height: var(--body-small-line-height, 24px);
            font-weight: var(--body-small-font-weight, 400);
            position: relative;
          "
        >
          로그아웃
  </a>
        <ButtonStyleFilled
          styleVariant="filled"
          style="
            background: var(--6b6b6b, #000000);
            border-color: var(--7b95b7, #6b6b6b);
            flex-shrink: 0;
          "
          name="생성하기"
        ></ButtonStyleFilled>
      </div>
    </div>
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
                    height: 40px;
                    font-size: 16pt;
                  "
                >
                  <span>
                    <span class="div-2-span2"><br /></span>
                    <span class="div-2-span3">
                      생성 요청했습니다.
                      <br />
                      완료되면 화면이 자동으로 변환됩니다.
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