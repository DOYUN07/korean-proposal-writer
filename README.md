# 제안서 라이터

Korean Proposal Writer

고객 요구와 피드백을 반영한 제안서 작성

## 개요

고객·바이어의 요구, 제안요청서인 RFP, 회사 자료와 메모를 바탕으로 공공·민간 제안서를 작성하고 보강합니다. 고객이 해결하려는 문제와 구매·평가 기준을 파악하여, 제공할 해결책과 수행 가능성, 선택해야 할 이유를 구체적으로 설명합니다.

RFP가 있으면 요구사항·평가항목·제출 규격을 분석하고 본문 내용에 대응시킵니다. 필요한 자료조사 후 제안전략과 스토리보드를 구성하고, 회사 역량·기술 및 수행 방안·산출물·검수·조직·일정·비용·사업관리·지원 내용을 작성합니다. 설득력과 함께 실행계획의 현실성도 검토합니다.

사용자가 제공한 『사업 수주를 부르는 제안 필승 가이드』 발췌 내용을 재구성한 실무 스킬을 활용합니다. 핵심 메시지, 페이지 구성, 부문별 작성, 표준제안서 재사용과 평가항목 중심의 요약 방법을 적용하되, 실제 RFP와 지정 양식을 우선합니다.

최종 파일 전에 초안의 약한 부분, 보완 이유와 추천안을 보여드리고 핵심 질문을 한 번에 최대 3개 제시합니다. 답변을 반영하여 본문과 관련 수치·일정·조건을 함께 수정합니다. “질문 없이 바로 작성”이나 “추천안대로 진행”도 가능합니다.

기본 결과물은 편집 가능한 Word 제안서입니다. 제안요약서를 요청하거나 RFP에서 요구하면 함께 작성하며, 발표자료와는 구분합니다. 내용·수치·서식을 검토하고 후속 수정은 문서 파일에 반영합니다.

확인되지 않은 실적·인증·성능이나 경쟁사의 약점을 만들지 않습니다. 파일 처리와 시각 검증은 실행 환경에서 가능한 범위로 수행하며, 실제 계약 체결이나 입찰 제출은 작성 작업에 포함되지 않습니다.

시작 예시: “첨부 RFP와 회사 소개자료로 제안서를 작성해줘. 보완점을 먼저 논의하고, 제안서와 요약서를 각각 파일로 만들어줘.”

## 기본 진행 흐름

자료와 공고 분석 → 필요한 조사 → 초안 준비 → 보완 이유와 추천안 제시 → 최대 3개 질문 → 사용자 피드백 반영 → 내용과 파일 검토 → DOCX 전달

단순 수정이나 실질적인 보완점이 없는 경우에는 질문을 만들지 않습니다. 사용자가 질문 생략 또는 추천안 적용을 요청하면 해당 선택을 따릅니다.

## 설치 및 적용 방법

### 준비 사항

- Codex CLI에서 아래 `plugin` 명령을 지원해야 합니다. `codex plugin --help`로 확인할 수 있습니다.
- GitHub 소스를 가져오려면 Git과 인터넷 연결이 필요합니다. 실행 호스트에는 정상적으로 로그인되어 있어야 합니다.
- DOCX 출력에는 호스트의 파일 실행·문서 생성 기능이 필요합니다. 설치만으로 검색·파일 변환 도구가 추가되지는 않습니다.

아래 두 방법 중 하나를 선택하세요. 같은 스킬을 플러그인과 수동 복사 방식으로 중복 설치하면 선택 목록에 같은 이름이 여러 번 보일 수 있습니다.

### 방법 1 플러그인 전체 설치

터미널 또는 Windows PowerShell에서 실행합니다. 이 저장소의 `.agents/plugins/marketplace.json`이 플러그인 목록을 제공합니다.

```sh
codex plugin marketplace add DOYUN07/korean-proposal-writer
codex plugin add proposal-writer@korean-proposal-writer
codex plugin list --json
```

마지막 명령에서 `proposal-writer`의 설치 상태를 확인하세요. 설치 후 새 세션을 시작하고, 데스크톱 앱에서 보이지 않으면 앱을 다시 시작합니다. CLI의 `/plugins`에서도 설치 목록과 활성화 상태를 확인할 수 있습니다. 데스크톱의 플러그인 선택 화면에서는 표시된 이름인 **제안서 라이터**를 선택합니다.

저장소 이름 `korean-proposal-writer`는 마켓플레이스 이름이고, `proposal-writer`는 설치할 플러그인의 이름입니다. 명령에서 두 이름을 바꾸어 쓰지 마세요.

### 방법 2 로컬 스킬만 복사

플러그인 관리 기능 대신 로컬 스킬로 사용하려는 경우의 대안입니다. 아래는 Windows PowerShell 예시이며, **현재 폴더 아래에 새 저장소 폴더가 생성**됩니다.

```powershell
git clone https://github.com/DOYUN07/korean-proposal-writer.git
if ($LASTEXITCODE -ne 0) { throw '저장소 복제에 실패했습니다.' }
Set-Location ./korean-proposal-writer
$repoRoot = (Get-Location).Path
$skillRoot = Join-Path $HOME '.agents/skills'
$skillNames = @('proposal-writer', 'rfp-proposal-practice')
foreach ($skillName in $skillNames) {
    $target = Join-Path $skillRoot $skillName
    if (Test-Path -LiteralPath $target) {
        throw "같은 이름의 스킬이 이미 있습니다. 기존 내용을 확인하세요: $target"
    }
}
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
foreach ($skillName in $skillNames) {
    $source = Join-Path $repoRoot ('skills/' + $skillName)
    Copy-Item -LiteralPath $source -Destination $skillRoot -Recurse
}
```

`SKILL.md` 한 파일만 옮기지 말고 `references`를 포함한 스킬 폴더 전체를 복사해야 합니다. `proposal-writer`와 `rfp-proposal-practice` 두 폴더를 모두 복사해야 RFP 실무 연결이 유지됩니다.

macOS·Linux에서도 사용자 폴더의 `~/.agents/skills/` 아래로 같은 스킬 폴더를 복사할 수 있습니다. 특정 프로젝트에서만 쓰려면 사용자 경로 대신 해당 프로젝트의 `.agents/skills/`를 사용합니다. 수동 복사 방식은 소개 화면을 갖춘 플러그인을 등록하는 방식과 다릅니다.

복사 후 새 Codex 세션에서 `/skills` 또는 스킬 선택 목록을 확인합니다. 보이지 않으면 앱을 다시 시작합니다.

### 적용 후 사용 예시

공고·RFP·지정 양식·회사 소개 등 필요한 자료를 첨부하고 요청합니다. CLI 또는 IDE의 스킬 직접 호출 예시는 다음과 같습니다. 데스크톱에서는 플러그인·스킬 선택 목록에서 선택한 뒤 같은 요청을 입력해도 됩니다.

```text
$proposal-writer 첨부 RFP와 회사 자료를 바탕으로 제안서를 작성해줘. 최종 파일 전에 보완점과 추천안을 먼저 설명하고 질문해줘.
```

가상기업 테스트는 다음처럼 명시합니다.

```text
첨부 공고에 맞는 가상기업으로 테스트해줘.
실제 공고 조건과 가상기업 설정은 구분해줘.
초안을 준비한 뒤 보완 제안과 질문을 먼저 보여주고,
내 피드백을 반영해 본문과 요약서를 각각 DOCX로 만들어줘.
```

자료 분석과 초안 준비 후 중요한 보완점이 있으면 이유·추천안·최대 3개 질문이 제시됩니다. 답변하면 관련 본문과 수치를 수정한 뒤 파일을 전달합니다. 바로 결과를 원하면 “질문 없이 현재 정보로 작성해줘”라고 요청할 수 있습니다.

### 업데이트와 제거

Git 마켓플레이스의 최신 소스를 가져오는 명령입니다.

```sh
codex plugin marketplace upgrade korean-proposal-writer
codex plugin list --json
```

새 세션에서 버전을 확인하세요. 설치된 버전이 갱신되지 않으면 `/plugins`에서 상태를 확인하고, 필요할 때 다음 순서로 재설치합니다.

```sh
codex plugin remove proposal-writer@korean-proposal-writer
codex plugin add proposal-writer@korean-proposal-writer
```

플러그인만 제거하려면 위 `remove` 명령을 사용합니다. 마켓플레이스 등록까지 제거하려면 다음을 실행합니다.

```sh
codex plugin marketplace remove korean-proposal-writer
```

스킬을 수동 복사했다면 `git pull --ff-only`로 소스를 갱신한 뒤 설치했던 폴더를 백업하고 변경 내용을 반영합니다. 기존 폴더를 덮어쓰면 개인 수정이 사라질 수 있으므로 복사 예시는 기존 폴더가 있으면 중단하도록 되어 있습니다. 수동 스킬은 플러그인 제거 명령으로 지워지지 않습니다.

### 적용되지 않을 때

- `plugin` 명령이 없으면 사용하는 Codex 버전과 공식 설치 안내를 확인하거나 로컬 스킬 복사 방법을 사용합니다.
- 파일이 있는데 스킬이 안 보이면 폴더 계층과 `SKILL.md` 위치를 확인하고 새 세션을 시작합니다.
- 참고문서를 못 찾으면 스킬 폴더 전체를 복사했는지 확인합니다.
- DOCX가 생성되지 않으면 해당 호스트의 파일 실행·문서 생성 기능을 확인합니다.
- 일반 ChatGPT 채팅에 GitHub URL을 붙이는 것만으로 플러그인이 설치되지는 않습니다. 조직 배포는 관리자의 GitHub 마켓플레이스 가져오기 절차를 따릅니다.

설치 명령 구문은 공식 문서와 현재 CLI 도움말을 대조했습니다. 이용자 계정에 대한 실제 설치·삭제는 이 저장소 준비 과정에서 실행하지 않았습니다.

공식 안내: [플러그인 패키징과 마켓플레이스](https://developers.openai.com/plugins/build/plugins), [CLI 명령](https://learn.chatgpt.com/docs/cli/reference), [스킬 경로와 호출](https://learn.chatgpt.com/docs/build-skills), [플러그인 사용](https://learn.chatgpt.com/docs/plugins).

## 소스 구성

- `.agents/plugins/marketplace.json`: GitHub 마켓플레이스 설치 목록
- `plugin.json`: 플러그인 기본 정보와 소개
- `.codex-plugin/plugin.json`: 호환용 메타데이터
- `skills/proposal-writer/SKILL.md`: 기본 작성 지침
- `skills/proposal-writer/references/`: 조사, 피드백, 가독성, 공고와 최종 점검 기준
- `skills/rfp-proposal-practice/SKILL.md`: RFP 분석, 스토리보드, 부문별 집필과 평가 대응 요약
- `scripts/package_plugin.py`: 소스 검증과 ZIP 생성
- `LICENSE`: MIT 라이선스

## 실행 환경과 결과물

이 저장소는 작성 지침으로 구성된 스킬 플러그인의 소스입니다. 독립 실행형 문서 생성 프로그램이나 자체 검색 서버를 포함하지 않습니다. 검색, 파일 열람, DOCX 생성과 렌더링은 사용하는 호스트에서 제공하는 도구에 의존합니다.

공식 양식과 제출 규정이 기본 문서 구성보다 우선합니다. 파일 생성 기능이 없는 환경에서는 해당 제한을 알리고 작성한 본문을 제공합니다. GitHub 소스를 수정해도 계정에 설치된 플러그인이 자동으로 업데이트되지는 않습니다.

## 패키지 만들기

Python 3.9 이상에서 별도 패키지 설치 없이 실행할 수 있습니다.

```sh
python scripts/package_plugin.py
```

검증을 통과하면 `dist/proposal-writer-0.1.7.zip`을 생성합니다. ZIP에는 플러그인 메타데이터, 스킬, 참고문서, 라이선스만 포함됩니다. 이 명령은 원격 플러그인을 생성하거나 업데이트하지 않습니다.

## 버전

현재 소스 버전: **0.1.7**

2026년 10월 22일 계정에 저장된 최신 릴리스의 소스를 기준으로 구성했습니다. 작성 결과물, 기업 자료, 서명, 인증 증명, API 키와 계정 토큰은 포함하지 않습니다.

## 참고자료와 라이선스

이 저장소의 작성 지침과 도구는 MIT 라이선스로 제공합니다. 누구나 사용·수정·배포할 수 있으며, 라이선스의 저작권 및 허가 고지를 유지해야 합니다.

RFP 실무 지침은 사용자가 제공한 『사업 수주를 부르는 제안 필승 가이드』 발췌 자료를 참고해 재구성했습니다. 책의 원문 TXT·스캔 사진은 포함하지 않습니다. 연결된 서적·문서·외부 사이트의 원문은 각 권리자의 조건을 따르며, 이 저장소의 MIT 라이선스가 해당 원문에 적용되는 것은 아닙니다.
