<script>
  import ButtonStyleFilled from "../join/ButtonStyleFilled.svelte";
  import RequestFilled from "../../components/button/request_filled.svelte";
  import PlaceholderImage from "./PlaceholderImage.svelte";
  import Header from "../../components/header/header_login.svelte";
  import StarRating from "../../components/rating/StarRating.svelte";
  import SaveImage from "../../components/button/result_save.svelte";
  import { onMount } from 'svelte';
  let className = "";
  export { className as class };
  export let style;
  let gt_stretch_path = "https://i0.wp.com/www.printmag.com/wp-content/uploads/2021/02/4cbe8d_f1ed2800a49649848102c68fc5a66e53mv2.gif?fit=476%2C280&ssl=1";
  let voice_stretch_path = "https://blog.teamtailor.com/hs-fs/hubfs/giphy%20(3).gif?width=500&height=245&name=giphy%20(3).gif";
  let condition_stretch_path = "https://social-phinf.pstatic.net/20211122_62/1637573927058bhdFb_GIF/23ee09341fb3d26c2b57efc4dd3b928ea3364f68.gif";
  
  let results = [];
  let id = sessionStorage.getItem('id'); // 수정된 부분
  let latest_id = sessionStorage.getItem('latest_id'); // 수정된 부분

  onMount(async () => {
        const token = sessionStorage.getItem('auth_token'); // sessionStorage에서 토큰 가져오기
    const response = await fetch(`http://175.45.194.59:5050/api/v1/mz-request/${id}/mz-result/${latest_id}`, {
      method: 'GET',
      headers: {
                'Token': token,
      },
      
    });

    if (response.ok) {
      const data = await response.json();
      results = data.mz_result; // 서버로부터 받은 데이터로 items 업데이트
      console.log(token);
    } else if(response.status === 400) {
      alert("데이터베이스 에러");
    }else {
      console.error('데이터를 가져오는 데 실패했습니다.');
      alert("요청 중 에러가 발생했습니다.")
    }
  });

  async function handleSubmit(event) {
    event.preventDefault();

  }
  


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
            style="flex-shrink: 0; width: 390px; height: 390px"
            targetPath={results.voice_image_url}
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
          <StarRating ABtype='voice' result_id={id} latest_id={latest_id} />
          <SaveImage targetImage= {results.voice_image_url}/>
            
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
            targetPath={results.condition_image_url}
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
          <StarRating ABtype= 'condition' result_id={id} latest_id={latest_id}/>
          <SaveImage targetImage={results.condition_image_url} />
            
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
                height: 250px;
                position: absolute;
                left: 0px;
                top: 105px;
              "
              targetPath={gt_stretch_path};
            ></PlaceholderImage>
          </div>
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
              style="
                width: 393px;
                height: 250px;
                position: absolute;
                left: 0px;
                top: 105px;
              "
              targetPath={results.voice_gif_url};
            ></PlaceholderImage>
          </div>
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
              style="
                width: 393px;
                height: 250px;
                position: absolute;
                left: 0px;
                top: 105px;
              "
              targetPath={results.condition_gif_url};
            ></PlaceholderImage>
          </div>
        </div>
      </div>
      <div
        style="flex-shrink: 0; width: 608.89px; height: 48px; position: static"
      >
        <RequestFilled
          styleVariant="filled"
          style="
            background: var(--7b95b7, #6b6b6b);
            width: 190px;
            position: absolute;
            left: 360.56px;
            top: 754px;
          "
          name="다시 생성하기"
        ></RequestFilled>
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
          설문조사
        </div>
  <div style="text-align:center; font-size: 20pt; "> 
    안녕하세요! 사용자의 목소리를 기반으로 가상의 얼굴을 생성하는 서비스, <span><strong>Voice2Face</strong></span>를 개발 중인 <span><strong>Make Zenerator</strong></span>팀입니다.
    <br />
    ~서비스에 대한 간단 소개 및 향후 계획~
    <br /><br />
    지금까지의 서비스 이용 경험을 바탕으로 아래의 설문 조사에 참여해주시면 감사드리겠습니다.
    <br />
    설문 예상 소요 시간은 <span><strong>약 5분 내외</strong></span>이며  
    <br /> 
    참여하신 분들 중 추첨을 통해 5분께 <span><strong>스타벅스 카페 아메리카노</strong></span> 기프티콘을 드릴 예정입니다
    <br />
    생성된 이미지 결과별로 설문 가능합니다. 많이 작성해주시면 확률이 올라갑니다.
    <br />
    (50명 넘으면 치킨으로 바뀔수도..? ^^)</div>

    <div style="items-align:center; ">
      

    </div>

    
</div>
