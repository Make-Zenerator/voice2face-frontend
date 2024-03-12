module.exports = {
    apps: [{
      script: './build/index.js', // 실행할 스크립트 파일
      instances: 1, // 인스턴스 수
      autorestart: true, // 자동 재시작 여부
      watch: false, // 파일 변경 감지 여부
      env: { // 환경 변수 설정
        NODE_ENV: 'development',
        PORT: 3000
      },
      env_production: { // 프로덕션 환경 변수 설정
        NODE_ENV: 'production',
        PORT: 80
      }
    }]
  };
  