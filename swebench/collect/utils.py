import urllib
        delay = 10
                # all prs done
            # except urllib.error.URLError as e:
            #     # logger.error(
            #     #     f"[{self.owner}/{self.name}] Error processing page {page} "
            #     #     f"w/ token {self.token[:10]} - {e.reason}"
            #     # )
            #     logger.error(f"URLError caught, {e.reason}")
            #     logger.error(f"Retrying in {delay} seconds...")
            #     time.sleep(delay)
                # waiting for api rate limit reset
from unidiff import PatchSet

class PatchManager:
    def __init__(self, patch: str):
        """
        初始化 PatchManager 并解析补丁内容。

        Args:
            patch (str): 输入的补丁内容。
        """
        self.patch = patch
        self.patch_set = PatchSet(patch)
        self.hunks = self._parse_patch()

    def _parse_patch(self):
        """
        解析补丁内容，将每个 hunk 和对应的文件路径组合成可直接应用的 patch。

        Returns:
            list: 每个元素是一个包含文件路径和 hunk 内容的字典。
        """
        parsed_hunks = []
        for patched_file in self.patch_set:
            for hunk in patched_file:
                # 生成单独的 hunk 内容
                if patched_file.source_file == "/dev/null":
                    # print(hunk)
                    hunk_text = f"diff --git {patched_file.source_file} {patched_file.target_file}\nnew file mode 100644\n--- {patched_file.source_file}\n+++ {patched_file.target_file}\n{str(hunk)}"
                else:
                    hunk_text = f"diff --git {patched_file.source_file} {patched_file.target_file}\n--- {patched_file.source_file}\n+++ {patched_file.target_file}\n{str(hunk)}"

                parsed_hunks.append(hunk_text)
        return parsed_hunks




def extract_patches(pull: dict, repo: Repo, mode:str) -> tuple[str, str]:
    patchManager = PatchManager(patch)
    if mode == "llm":
        for hunk in PatchSet(patch):
        return patch_fix, patch_test
    elif mode == "new":
        for hunk in patchManager.hunks:
            if any(
                test_word in hunk for test_word in
                ['test', 'tests', 'e2e', 'testing']
            ):
                patch_test += str(hunk)
            else:
                patch_fix += str(hunk)
        return patch_fix, patch_test
    else:
        for hunk in PatchSet(patch):
            if any(
                test_word in hunk.path for test_word in
                ['test', 'tests', 'e2e', 'testing']
            ):
                patch_test += str(hunk)
            else:
                patch_fix += str(hunk)
            # patch_fix += str(hunk)
        return patch_fix, patch_test
    # return patch_fix
