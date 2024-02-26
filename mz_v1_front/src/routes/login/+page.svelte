<script>
  import ButtonStyleFilled from "../join/ButtonStyleFilled.svelte";
  import PlaceholderImage from "./PlaceholderImage.svelte";
  import Header from "../../components/header_non.svelte";
  let className = "";
  export { className as class };
  export let style;
</script>
<div
  style="{'background: var(--neutral-0, #ffffff); display: flex; flex-direction: column; gap: 160px; align-items: center; justify-content: flex-start; height: 845px; position: relative; ' + style}"
>
  <Header/>
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
                position: relative;
              "
            >
              <div
                style="
                  color: #000000;
                  text-align: center;
                  font-family: 'DmSans-Bold', sans-serif;
                  font-size: 46px;
                  line-height: 40px;
                  font-weight: 700;
                  position: relative;
                  width: 451px;
                  height: 40px;
                "
              >
                로그인
              </div>
              <div
                style="
                  display: flex;
                  flex-direction: column;
                  gap: 10px;
                  align-items: flex-start;
                  justify-content: flex-start;
                  flex-shrink: 0;
                  position: relative;
                "
              >
                <div
                  style="
                    color: #000000;
                    text-align: left;
                    font-family: 'DmSans-Medium', sans-serif;
                    font-size: 19px;
                    line-height: 40px;
                    font-weight: 500;
                    position: relative;
                    width: 125px;
                    height: 23px;
                    display: flex;
                    align-items: center;
                    justify-content: flex-start;
                  "
                >
                  이메일 주소
                </div>
                <div
                  style="
                    background: #ffffff;
                    border-radius: 10px;
                    border-style: solid;
                    border-color: #000000;
                    border-width: 1px;
                    padding: 1px 43px 1px 43px;
                    display: flex;
                    flex-direction: row;
                    gap: 10px;
                    align-items: center;
                    justify-content: flex-start;
                    flex-shrink: 0;
                    width: 337px;
                    position: relative;
                    overflow: hidden;
                  "
                >
                  <div
                    style="
                      color: rgba(0, 0, 0, 0.4);
                      text-align: center;
                      font-family: 'DmSans-Medium', sans-serif;
                      font-size: 14px;
                      line-height: 40px;
                      font-weight: 500;
                      position: relative;
                      width: 250px;
                      display: flex;
                      align-items: center;
                      justify-content: center;
                    "
                  >
                    이메일 입력
                  </div>
                </div>
                <div
                  style="
                    color: #000000;
                    text-align: left;
                    font-family: 'DmSans-Medium', sans-serif;
                    font-size: 19px;
                    line-height: 40px;
                    font-weight: 500;
                    position: relative;
                    width: 125px;
                    height: 23px;
                    display: flex;
                    align-items: center;
                    justify-content: flex-start;
                  "
                >
                  비밀번호
                </div>
                <div
                  style="
                    background: #ffffff;
                    border-radius: 10px;
                    border-style: solid;
                    border-color: #000000;
                    border-width: 1px;
                    padding: 1px 43px 1px 43px;
                    display: flex;
                    flex-direction: row;
                    gap: 10px;
                    align-items: center;
                    justify-content: flex-start;
                    flex-shrink: 0;
                    width: 337px;
                    position: relative;
                    overflow: hidden;
                  "
                >
                  <div
                    style="
                      color: rgba(0, 0, 0, 0.4);
                      text-align: center;
                      font-family: 'DmSans-Medium', sans-serif;
                      font-size: 14px;
                      line-height: 40px;
                      font-weight: 500;
                      position: relative;
                      width: 248px;
                      display: flex;
                      align-items: center;
                      justify-content: center;
                    "
                  >
                    비밀번호 입력
                  </div>
                </div>
              </div>
            </div>
            <ButtonStyleFilled
              styleVariant="filled"
              style=
              "background: var(--7b95b7, #6b6b6b);
              flex-shrink: 0"
              name="로그인"
            ></ButtonStyleFilled>
          </div>
          <div
            style="
              background: #d9d9d9;
              flex-shrink: 0;
              width: 100px;
              height: 100px;
              position: relative;
            "
          ></div>
        </div>
        <PlaceholderImage
          style="flex-shrink: 0; width: 564px; height: 405px"
        ></PlaceholderImage>
      </div>
    </div>
  </div>
</div>