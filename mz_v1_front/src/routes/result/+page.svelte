<script>
  import ButtonStyleFilled from "../join/ButtonStyleFilled.svelte";
  import PlaceholderImage from "./PlaceholderImage.svelte";
  import Header from "../../components/header_login.svelte";
  import StarRating from "../../components/rating/StarRating.svelte";
  import SaveImage from "../../components/button/result_save.svelte";
  let className = "";
  export { className as class };
  export let style;
  let voice_face_path = "/join/placeholder-image.svg";
  let condition_face_path = "/join/placeholder-image.svg";

  
</script>
<div
  style="{'background: var(--neutral-0, #ffffff);padding: 0px 0px 120px 0px; display: flex; flex-direction: column; gap: 30px; align-items: center; justify-content: flex-start; position: relative; ' + style}"
>
  <Header/>
  <img
    class="image-22"
    style="
      flex-shrink: 0;
      width: 196px;
      height: 120px;
      position: relative;
      object-fit: cover;
    "
    src="/join/image-21.png"
  />
  <div
    style="
      display: flex;
      flex-direction: column;
      gap: 159px;
      align-items: center;
      justify-content: flex-start;
      flex-shrink: 0;
      position: relative;
    "
  >
    <div
      style="
        display: flex;
        flex-direction: row;
        gap: 211px;
        align-items: flex-start;
        justify-content: flex-start;
        flex-shrink: 0;
        position: relative;
      "
    >
      <div
        style="
          display: flex;
          flex-direction: column;
          gap: 13px;
          align-items: center;
          justify-content: flex-start;
          flex-shrink: 0;
          position: relative;
        "
      >
        <div
          style="
            display: flex;
            flex-direction: column;
            gap: 15px;
            align-items: center;
            justify-content: flex-start;
            flex-shrink: 0;
            position: relative;
          "
        >
          <div
            style="
              display: flex;
              flex-direction: column;
              gap: 18px;
              align-items: flex-start;
              justify-content: flex-start;
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
                width: 294px;
                height: 40px;
              "
            >
              Voice
            </div>
            <div
              style="
                color: #8c8686;
                text-align: center;
                font-family: var(
                  --body-large-font-family,
                  'DmSans-Regular',
                  sans-serif
                );
                font-size: var(--body-large-font-size, 20px);
                line-height: var(--body-large-line-height, 32px);
                font-weight: var(--body-large-font-weight, 400);
                position: relative;
                width: 294px;
              "
            >
              목소리에 어울리는 얼굴
            </div>
          </div>
          <PlaceholderImage
            style="flex-shrink: 0; width: 393px; height: 393px";
            filename={voice_face_path}
          ></PlaceholderImage>
        </div>
        <div
          style="
            display: flex;
            flex-direction: row;
            gap: 70px;
            align-items: flex-start;
            justify-content: flex-start;
            flex-shrink: 0;
            position: relative;
          "
        >
          <div
            style="
              display: flex;
              flex-direction: column;
              align-items: center;
              justify-content: flex-start;
              flex-shrink: 0;
              position: relative;
            "
          >
          <div
            style="
              display: flex;
              flex-direction: row;
              gap: 11px;
              align-items: flex-end;
              justify-content: flex-start;
              flex-shrink: 0;
              position: relative;
            "
          >
          <StarRating />
          <SaveImage targetImage= {voice_face_path}/>
            
          </div>
            
          </div>
          
        </div>
      </div>
      <div
        style="
          display: flex;
          flex-direction: column;
          gap: 13px;
          align-items: center;
          justify-content: flex-start;
          flex-shrink: 0;
          position: relative;
        "
      >
        <div
          style="
            display: flex;
            flex-direction: column;
            gap: 15px;
            align-items: center;
            justify-content: flex-start;
            flex-shrink: 0;
            position: relative;
          "
        >
          <div
            style="
              display: flex;
              flex-direction: column;
              gap: 18px;
              align-items: flex-start;
              justify-content: flex-start;
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
                width: 294px;
                height: 40px;
              "
            >
              Condition
            </div>
            <div
              style="
                color: #8c8686;
                text-align: center;
                font-family: var(
                  --body-large-font-family,
                  'DmSans-Regular',
                  sans-serif
                );
                font-size: var(--body-large-font-size, 20px);
                line-height: var(--body-large-line-height, 32px);
                font-weight: var(--body-large-font-weight, 400);
                position: relative;
                width: 294px;
              "
            >
              성별, 나이만으로 만들어진 얼굴
            </div>
          </div>
          <PlaceholderImage
            style="flex-shrink: 0; width: 390px; height: 390px"
            targetPath={condition_face_path}
          ></PlaceholderImage>
        </div>
        <div
          style="
            display: flex;
            flex-direction: row;
            gap: 70px;
            align-items: flex-start;
            justify-content: flex-start;
            flex-shrink: 0;
            position: relative;
          "
        >
          <div
            style="
              display: flex;
              flex-direction: column;
              align-items: center;
              justify-content: flex-start;
              flex-shrink: 0;
              position: relative;
            "
          >
          <div
            style="
              display: flex;
              flex-direction: row;
              gap: 11px;
              align-items: flex-end;
              justify-content: flex-start;
              flex-shrink: 0;
              position: relative;
            "
          >
          <StarRating />
          <SaveImage saveImage={condition_face_path} />
            
          </div>
            
          </div>
          
        </div>
      </div>
    </div>
    <div
      style="
        display: flex;
        flex-direction: column;
        gap: 119px;
        align-items: center;
        justify-content: flex-start;
        flex-shrink: 0;
        position: relative;
      "
    >
      <div
        style="
          display: flex;
          flex-direction: column;
          gap: 10px;
          align-items: center;
          justify-content: flex-start;
          flex-shrink: 0;
          position: relative;
        "
      >
        <div
          style="
            color: #000000;
            text-align: center;
            font-family: 'DmSans-Bold', sans-serif;
            font-size: 52px;
            line-height: 76px;
            font-weight: 700;
            position: relative;
            width: 742px;
            height: 65px;
          "
        >
          Service Coming soon
        </div>
        <div
          style="
            color: #8c8686;
            text-align: center;
            font-family: var(
              --body-large-font-family,
              'DmSans-Regular',
              sans-serif
            );
            font-size: var(--body-large-font-size, 20px);
            line-height: var(--body-large-line-height, 32px);
            font-weight: var(--body-large-font-weight, 400);
            position: relative;
            width: 615px;
            height: 150px;
          "
        >
          생성된 이미지를 영상에 입힐 수 있습니다
          
        </div>
        <div
          style="
            display: flex;
            flex-direction: row;
            gap: 77px;
            align-items: flex-end;
            justify-content: flex-start;
            flex-shrink: 0;
            position: relative;
          "
        >
          <div
            style="
              flex-shrink: 0;
              width: 393px;
              height: 498px;
              position: relative;
            "
          >
            <div
              style="
                display: flex;
                flex-direction: column;
                gap: 18px;
                align-items: flex-start;
                justify-content: flex-start;
                position: absolute;
                left: 49.5px;
                top: 0px;
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
                  width: 294px;
                  height: 40px;
                "
              >
                Original
              </div>
              <div
                style="
                  color: #8c8686;
                  text-align: center;
                  font-family: var(
                    --body-large-font-family,
                    'DmSans-Regular',
                    sans-serif
                  );
                  font-size: var(--body-large-font-size, 20px);
                  line-height: var(--body-large-line-height, 32px);
                  font-weight: var(--body-large-font-weight, 400);
                  position: relative;
                  width: 294px;
                "
              >
                스트레칭 동영상
              </div>
            </div>
            <PlaceholderImage
              style="
                width: 393px;
                height: 393px;
                position: absolute;
                left: 0px;
                top: 105px;
              "
            ></PlaceholderImage>
          </div>
          <div
            style="
              display: flex;
              flex-direction: column;
              gap: 15px;
              align-items: center;
              justify-content: flex-start;
              flex-shrink: 0;
              position: relative;
            "
          >
            <div
              style="
                display: flex;
                flex-direction: column;
                gap: 18px;
                align-items: flex-start;
                justify-content: flex-start;
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
                  width: 294px;
                  height: 40px;
                "
              >
                Voice
              </div>
              <div
                style="
                  color: #8c8686;
                  text-align: center;
                  font-family: var(
                    --body-large-font-family,
                    'DmSans-Regular',
                    sans-serif
                  );
                  font-size: var(--body-large-font-size, 20px);
                  line-height: var(--body-large-line-height, 32px);
                  font-weight: var(--body-large-font-weight, 400);
                  position: relative;
                  width: 294px;
                "
              >
                목소리에 어울리는 얼굴
              </div>
            </div>
            <PlaceholderImage
              style="flex-shrink: 0; width: 393px; height: 393px"
            ></PlaceholderImage>
          </div>
          <div
            style="
              display: flex;
              flex-direction: column;
              gap: 15px;
              align-items: center;
              justify-content: flex-start;
              flex-shrink: 0;
              position: relative;
            "
          >
            <div
              style="
                display: flex;
                flex-direction: column;
                gap: 18px;
                align-items: flex-start;
                justify-content: flex-start;
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
                  width: 294px;
                  height: 40px;
                "
              >
                Condition
              </div>
              <div
                style="
                  color: #8c8686;
                  text-align: center;
                  font-family: var(
                    --body-large-font-family,
                    'DmSans-Regular',
                    sans-serif
                  );
                  font-size: var(--body-large-font-size, 20px);
                  line-height: var(--body-large-line-height, 32px);
                  font-weight: var(--body-large-font-weight, 400);
                  position: relative;
                  width: 294px;
                "
              >
                성별, 나이만으로 만들어진 얼굴
              </div>
            </div>
            <PlaceholderImage
              style="flex-shrink: 0; width: 390px; height: 390px"
            ></PlaceholderImage>
          </div>
        </div>
      </div>
      <div
        style="flex-shrink: 0; width: 608.89px; height: 48px; position: static"
      >
        <ButtonStyleFilled
          styleVariant="filled"
          style="
            background: var(--7b95b7, #6b6b6b);
            width: 190px;
            position: absolute;
            left: 360.56px;
            top: 754px;
          "
          targetPath ="/infogather"
          name="다시 생성하기"
        ></ButtonStyleFilled>
        <ButtonStyleFilled
          styleVariant="filled"
          style="
            background: var(--7b95b7, #6b6b6b);
            width: 177.73px;
            position: absolute;
            left: 582.13px;
            top: 754px;
          "
          
          name="설문조사"
        ></ButtonStyleFilled>
        <ButtonStyleFilled
          styleVariant="filled"
          style="
            background: var(--7b95b7, #6b6b6b);
            width: 190px;
            position: absolute;
            left: 796.45px;
            top: 754px;
          "
          targetPath="/resultlist"
          name="결과 목록 보기"
        ></ButtonStyleFilled>
      </div>
    </div>
  </div>
</div>
