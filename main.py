import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, LLMConfig, JsonCssExtractionStrategy
from crawl4ai.extraction_strategy import JsonXPathExtractionStrategy
from dotenv import load_dotenv
import os
import json

load_dotenv()

async def non_llm_extraction():
    dummy_html = """
    <div class="MuiBox-root mui-1i8yr6r" role="tabpanel" id="simple-tabpanel-0" aria-labelledby="simple-tab-0"><div class="light-text-color MuiBox-root mui-0" id="content-to-copy"><div class="MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation6 dark-bg-color mui-1ucs79h" id="document-container" style="--Paper-shadow: 0px 3px 5px -1px rgba(0,0,0,0.2),0px 6px 10px 0px rgba(0,0,0,0.14),0px 1px 18px 0px rgba(0,0,0,0.12);"><button class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium mui-1ak6zjr" tabindex="0" type="button" aria-label="Display in full screen"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeSmall mui-1n9r5l7" focusable="false" aria-hidden="true" viewBox="0 0 24 24" data-testid="FullscreenIcon"><path d="M7 14H5v5h5v-2H7zm-2-4h2V7h3V5H5zm12 7h-3v2h5v-5h-2zM14 5v2h3v3h2V5z"></path></svg></button><p id="date" style="text-align: justify; margin: 12pt 21pt 24pt;">
	<span style="font-size: 12pt;"><b>November 4, 2019</b></span></p>
<p id="reference_no" style="text-align: center; margin: 6pt 7pt 24pt;">
	<span style="font-size: 14pt;">OPERATIONS MEMORANDUM NO. 030-19</span></p>
<div style="margin-left: 4.5em;">
	<table border="0" cellpadding="0" cellspacing="0"><colgroup></colgroup><colgroup><col width="120"></colgroup><colgroup><col width="20"></colgroup><colgroup><col width="550"></colgroup><tbody><tr height="21"><td height="21" valign="top" width="120">
					<span style="font-size: 13pt; color: rgb(0, 0, 0);">TO :&nbsp;</span>
</td><td valign="top" width="20">
					&nbsp;</td><td valign="top" width="550">
					<span style="font-size: 13pt; color: rgb(0, 0, 0);"><em>ACIR, Large Taxpayers Service</em></span>
</td></tr><tr height="21"><td height="21" valign="top">
					&nbsp;</td><td valign="top">
					&nbsp;</td><td valign="top">
					<span style="font-size: 13pt; color: rgb(0, 0, 0);"><em>All Regional Directors</em></span>
</td></tr><tr height="21"><td height="21" valign="top">
					&nbsp;</td><td valign="top">
					&nbsp;</td><td valign="top">
					<span style="font-size: 13pt; color: rgb(0, 0, 0);"><em>All Revenue District Officers</em></span>
</td></tr><tr height="21"><td height="21" valign="top">
					&nbsp;</td><td valign="top">
					&nbsp;</td><td valign="top">
					<span style="font-size: 13pt; color: rgb(0, 0, 0);"><em>All Others Concerned</em></span>
</td></tr><tr height="21"><td height="21" valign="top">
					&nbsp;</td><td valign="top">
					&nbsp;</td><td valign="top">
					&nbsp;</td></tr><tr height="21"><td height="21" valign="top">
					<span style="font-size: 13pt; color: rgb(0, 0, 0);">SUBJECT&nbsp;</span>
</td><td valign="top">
					<span style="font-size: 13pt; color: rgb(0, 0, 0);">:&nbsp;</span>
</td><td valign="top" width="550">
					<span style="font-size: 13pt; color: rgb(0, 0, 0);"><em>Price of Sugar at Millsite for the Week-Ending October 27, 2019 Issued by the Licensing and Monitoring Division, Regulation Department, Sugar Regulatory Administration</em></span>
</td></tr></tbody></table>
</div>
<p lang="en-US" style="text-indent: -81pt; margin: 0pt 14pt 0pt 126pt;">
	&nbsp;</p>
<p style="text-align: justify; text-indent: 36pt; margin: 6pt 9pt;">
	<span style="font-size: 13pt;">This Operations Memorandum (OM) is hereby issued in order to circularize the attached full text of the Price of Sugar at Millsite for the Week-Ending October 27, 2019 (Annex "A") provided to this Bureau by the Licensing and Monitoring Division, Regulation Department, Sugar Regulatory Administration (SRA), pursuant to Revenue Regulations No. 13-2015 dated October 12, 2015.</span></p>
<p style="text-align: justify; text-indent: 36pt; margin: 6pt 9pt;">
	<span style="font-size: 13pt;">It is informed that an RMC shall be issued within five (5) working days after the month of issuance of the weekly OMs, pursuant to Revenue Delegation Authority Order (RDAO) No. 3-2016 dated April 18, 2016.</span></p>
<p style="text-align: justify; text-indent: 36pt; margin: 6pt 9pt;">
	<span style="font-size: 13pt;">Accordingly, all revenue officials and employees are hereby enjoined to give this OM as wide a publicity as possible. </span></p>
<p style="text-align: justify; text-indent: 36pt; margin: 6pt 9pt;">
	<span style="font-size: 13pt;">For your information and guidance.</span></p>
<p lang="en-US" style="text-align: center; margin: 0pt 9pt 0pt 216pt;">
	&nbsp;</p>
<p lang="en-US" style="text-align: center; margin: 0pt 9pt 0pt 216pt;">
	<span style="font-size: 13pt; font-weight: bold;">(SGD.) ALFREDO V. MISAJON</span></p>
<p lang="en-US" style="text-align: center; margin: 0pt 9pt 0pt 216pt;">
	<span style="font-size: 13pt; font-style: italic;">Assistant Commissioner</span></p>
<p lang="en-US" style="text-align: center; margin: 0pt 9pt 0pt 216pt;">
	<span style="font-size: 13pt; font-style: italic;">Collection Service</span></p>
<p lang="en-US" style="text-align: right; margin: 0pt 9pt;">
	<span style="font-weight: bold; font-size: 12pt;">ANNEX A</span></p>
<p style="text-align: center; margin: 24pt 9pt 18pt;">
	<a href="https://cdn-usercontents.cdasiaonline.com/ckeditor_assets/private/attachments/operation_memoradum_no_30-19.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=P72YPKJESFXNVVHAAP5H%2F20250529%2Fsgp1%2Fs3%2Faws4_request&amp;X-Amz-Date=20250529T234211Z&amp;X-Amz-Expires=604800&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=16cddd09777d89873547431ef1513c6c2a5ccd494b29160efebc4e4e781840e4" target="_blank" style="color: rgb(0, 0, 0); pointer-events: auto;"><span style="color: rgb(0, 128, 0);"><strong><span style="font-style: italic; font-size: 12pt;"><u>Sugar Price at Millsite by Sugar Class</u></span></strong></span></a></p>
<p style="text-align: justify; text-indent: 36pt; margin: 6pt 9pt;">
	&nbsp;</p>
</div></div></div>
    """

    schema = JsonCssExtractionStrategy.generate_schema(
        html = dummy_html,
        llm_config=LLMConfig(
            provider= "gpt-4.1 nano",
            api_token= os.getenv("OPENAI_API_KEY")
        ),
        query= "From https://cdasiaonline.com/, I have shared a sample of one Law div with a title, date, to, subject, content, and annex. Please generate a schema for this law div.",
    )

    print(f"Generated Schema:{json.dumps(schema,indent=2)}")

    extraction_strategy = JsonCssExtractionStrategy(schema)

    config = CrawlerRunConfig(extraction_strategy=extraction_strategy)


    async with AsyncWebCrawler() as crawler:
        results: List[CrawlResulT] 
