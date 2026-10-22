from pathlib import Path
import hashlib,json,qrcode
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4,landscape
from reportlab.lib.colors import HexColor

ROOT=Path("/var/www/zippri-growth-os/production/site/agastya-native-brain-evidence/f3-8b/assets")
ROOT.mkdir(parents=True,exist_ok=True)
NAME="Agastya-F3-8B-Source-Token-Evidence-Certificate-R2.pdf"
DOI="10.5281/zenodo.23557660"
URL="https://doi.org/"+DOI
CERT="RI-AGASTYA-F3-8B-R2-20261022"
for alias,real in [('Lato','Regular'),('LatoBold','Bold'),('LatoHeavy','Heavy'),('LatoLight','Light')]:
 pdfmetrics.registerFont(TTFont(alias,"/usr/share/fonts/truetype/lato/Lato-"+real+".ttf"))
NAVY=HexColor("#061422"); PANEL=HexColor("#0B2233"); LINE=HexColor("#254458"); WHITE=HexColor("#F0F8FC")
MUTED=HexColor("#9CB9C8"); TEAL=HexColor("#63E5DA"); CYAN=HexColor("#4FC7E9")
GOLD=HexColor("#F5C477"); GREEN=HexColor("#75D5AB")
W,H=landscape(A4)
c=canvas.Canvas(str(ROOT/NAME),pagesize=(W,H),pageCompression=1,invariant=1)
c.setTitle("Agastya F3 R2 | 8B Source-Token Recorded Training Milestone Evidence Attestation")
c.setAuthor("Rabbit Industries Pvt Ltd")
c.setSubject("Publisher-issued research evidence attestation, not independent certification")
def box(x,y,w,h,bg,stroke=None,r=0):
 c.setFillColor(bg);c.setStrokeColor(stroke or bg);c.setLineWidth(1)
 c.roundRect(x,y,w,h,r,stroke=1 if stroke else 0,fill=1)
def word(x,y,s,size=10,col=WHITE,font="Lato",track=None):
 c.setFillColor(col)
 if track is not None:
  t=c.beginText(x,y);t.setFont(font,size);t.setCharSpace(track);t.textOut(s);c.drawText(t)
 else:c.setFont(font,size);c.drawString(x,y,s)
def hair(x1,y1,x2,y2,col=LINE):
 c.setStrokeColor(col);c.setLineWidth(.75);c.line(x1,y1,x2,y2)
def wallpaper():
 box(0,0,W,H,NAVY);box(15,15,W-30,H-30,NAVY,LINE,14);box(21,21,5,H-42,TEAL,r=2)
def doi_qr(x,y,side=38):
 q=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=1,border=1)
 q.add_data(URL);q.make(fit=True);a=q.get_matrix();step=side/len(a)
 box(x-7,y-7,side+14,side+14,WHITE,r=8)
 c.setFillColor(NAVY)
 for i,row in enumerate(a):
  for j,p in enumerate(row):
   if p:c.rect(x+j*step,y+(len(a)-i-1)*step,step+.06,step+.06,stroke=0,fill=1)
# Certificate
wallpaper()
box(38,H-70,34,34,PANEL,CYAN,9)
word(47,H-59,"RI",15,TEAL,"LatoHeavy")
word(84,H-47,"RABBIT INDUSTRIES",12,WHITE,"LatoHeavy",1.4)
word(84,H-63,"RESEARCH RECORDS / AGASTYA AGI",8,MUTED,"LatoBold",1.1)
word(W-245,H-49,"CERTIFICATE NO.",8,MUTED,"LatoBold",1)
word(W-245,H-67,CERT,9.1,TEAL,"LatoBold")
hair(40,H-90,W-40,H-90)
word(43,H-122,"PUBLISHER-ISSUED EVIDENCE ATTESTATION",9.6,GOLD,"LatoHeavy",1.3)
word(42,H-177,"Certificate of Recorded",32,WHITE,"LatoLight")
word(42,H-215,"Training Milestone",35,WHITE,"LatoHeavy")
word(42,H-267,"8,000,000,000",48,TEAL,"LatoHeavy")
word(45,H-290,"SOURCE TRAINING TOKENS",12,CYAN,"LatoHeavy",2.1)
word(45,H-316,"Candidate-training milestone recorded complete on 19 October 2026 (UTC).",10,MUTED)
box(43,H-397,500,59,PANEL,LINE,10)
word(59,H-359,"100.0%",18,GREEN,"LatoHeavy")
word(59,H-382,"Source-token target",9,MUTED)
hair(202,H-387,202,H-347)
word(220,H-359,"7,639",18,WHITE,"LatoBold")
word(220,H-382,"Optimizer step",9,MUTED)
hair(352,H-387,352,H-347)
word(366,H-359,"10,368,986",16,WHITE,"LatoBold")
word(366,H-382,"Exposure records",9,MUTED)
box(577,H-415,226,301,PANEL,LINE,17)
for radius,color in [(58,LINE),(48,CYAN),(40,LINE)]:
 c.setStrokeColor(color);c.setLineWidth(.7);c.circle(690,H-199,radius,stroke=1,fill=0)
c.setFont("LatoHeavy",30);c.setFillColor(TEAL);c.drawCentredString(690,H-196,"F3")
c.setFont("LatoBold",12);c.setFillColor(GOLD);c.drawCentredString(690,H-220,"R2")
word(599,H-277,"PUBLIC DOI",9.5,GOLD,"LatoHeavy",1.4)
word(599,H-302,DOI,12.4,WHITE,"LatoBold")
hair(599,H-321,784,H-321)
word(599,H-345,"VERIFIED PUBLIC RECORD",8.4,MUTED,"LatoBold",.8)
word(599,H-363,"Zenodo R2 / Published",9.9,GREEN,"LatoBold")
word(599,H-385,"SCAN DOI",7.6,MUTED,"LatoHeavy",1)
doi_qr(738,H-407,38)
word(45,119,"RABBIT INDUSTRIES PVT LTD",10,WHITE,"LatoBold",1)
word(45,103,"Issuer / self-attestation  |  Issued 22 October 2026",9.4,MUTED)
word(45,78,"Public evidence: "+URL,9.4,TEAL,"LatoBold")
c.linkURL(URL,(45,70,445,90),relative=0)
hair(44,60,W-44,60)
word(44,43,"SCOPE: internally recorded milestone; not independent certification or production approval.",8.7,GOLD,"LatoBold")
word(W-140,43,"PAGE 01 / 02",8.7,MUTED,"LatoBold")
c.showPage()
# Verification annex
wallpaper()
word(42,H-55,"AGASTYA / EVIDENCE VERIFICATION ANNEX",11,TEAL,"LatoHeavy",1.1)
word(W-230,H-55,CERT,9,MUTED,"LatoBold")
hair(41,H-73,W-41,H-73)
word(43,H-105,"Traceable. Citable. Precisely scoped.",21,WHITE,"LatoHeavy")
word(44,H-127,"Public evidence chain for the 8B source-token F3 R2 candidate training record.",10,MUTED)
box(43,H-376,483,228,PANEL,LINE,12)
word(61,H-171,"SOURCE EVIDENCE IDENTIFIERS",9.5,GOLD,"LatoHeavy",1)
rows=[
("TRAINING SOURCE TOKENS","8,000,000,000 of 8,000,000,000"),
("COMPLETION RECORD","2026-10-19 14:40:36 UTC"),
("OPTIMIZER STEP","7,639"),
("EXPOSURE LEDGER","10,368,986 records; reconciled"),
("CHECKPOINT BINARY SIZE","21,442,876,013 bytes"),
("PRODUCTION PROMOTION","NOT AUTHORIZED")]
for i,(k,v) in enumerate(rows):
 y=H-205-i*30
 word(61,y,k,8.2,MUTED,"LatoBold",.4)
 word(267,y,v,8.6,GREEN if i==0 else GOLD if i==5 else WHITE,"LatoBold")
 if i<5:hair(61,y-9,508,y-9)
box(542,H-376,257,228,PANEL,LINE,12)
word(557,H-171,"DOI / VERSION LINEAGE",9,GOLD,"LatoHeavy",.6)
for y,label,value,color in [
 (H-202,"R2 / CURRENT EVIDENCE",DOI,TEAL),
 (H-249,"R1 / HISTORICAL RECORD","10.5281/zenodo.23054425",WHITE),
 (H-296,"CONCEPT DOI / ALL VERSIONS","10.5281/zenodo.23054424",WHITE)]:
 word(557,y,label,8,MUTED,"LatoBold")
 word(557,y-19,value,10.4,color,"LatoBold")
hair(557,H-330,783,H-330)
word(557,H-350,"DOI independently resolves to Zenodo R2.",8.2,GREEN)
word(44,194,"SHA-256 / INTERNAL SOURCE RECORDS",9.5,GOLD,"LatoHeavy",1)
word(44,171,"Training-status JSON",8.7,MUTED,"LatoBold")
word(44,154,"c5c00ae774eccd17c39bd4da601c5ab0605af699bd2970b6cf3f3eb06987bbc3",8.1,WHITE)
word(44,132,"Checkpoint binary (digest recorded in metadata, not independently rehashed for issuance)",8.3,MUTED,"LatoBold")
word(44,115,"3e0ec187db627012e9e5eba9f73285b76f2185562b7c83841bc54e496e6325af",8.1,WHITE)
word(44,92,"PUBLIC VERIFICATION AND SCOPE",8.8,GOLD,"LatoHeavy",1)
word(44,76,"Verify PDF via portal SHA-256 manifest, then use DOI to examine the archived evidence.",8.3,WHITE)
word(44,63,"Publisher self-attestation only. Independent testing, model acceptance and deployment remain pending.",8,MUTED)
hair(42,49,W-42,49)
word(43,34,"8B = SOURCE TOKENS, NOT MODEL PARAMETERS  /  NO INDEPENDENT ACCREDITATION OR SIGNATURE CLAIMED",7.8,GOLD,"LatoBold")
word(W-142,34,"PAGE 02 / 02",8.5,MUTED,"LatoBold")
c.linkURL(URL,(543,H-235,797,H-200),relative=0)
c.showPage();c.save()

pdf=(ROOT/NAME).read_bytes()
sha=hashlib.sha256(pdf).hexdigest()
manifest={
 "schema":"rabbit-industries.agastya.public-evidence-certificate.v1",
 "certificate_id":CERT,
 "title":"Agastya F3 R2 8B Source-Token Candidate Training Evidence Attestation",
 "issuer":"Rabbit Industries Pvt Ltd",
 "issuer_role":"Publisher; self-attestation based on recorded internal training evidence",
 "issued_date":"2026-10-22",
 "recorded_milestone_timestamp_utc":"2026-10-19T14:40:36.126712+00:00",
 "version":"R2-F3-8B-SOURCE-TOKEN-CANDIDATE",
 "doi":DOI,
 "record":"https://zenodo.org/records/23557660",
 "concept_doi":"10.5281/zenodo.23054424",
 "historical_r1_doi":"10.5281/zenodo.23054425",
 "source_tokens":8000000000,"source_target_tokens":8000000000,"optimizer_step":7639,
 "exposure_records":10368986,"terminal_ledger_reconciled":True,
 "training_status_sha256":"c5c00ae774eccd17c39bd4da601c5ab0605af699bd2970b6cf3f3eb06987bbc3",
 "checkpoint_sha256_recorded":"3e0ec187db627012e9e5eba9f73285b76f2185562b7c83841bc54e496e6325af",
 "checkpoint_freshly_rehashed_for_issuance":False,
 "checkpoint_bytes":21442876013,
 "production_promotion_authorized":False,
 "independent_third_party_verification":"PENDING",
 "external_benchmark_acceptance":"PENDING",
 "certificate_pdf":{"filename":NAME,"bytes":len(pdf),"sha256":sha,"pages":2},
 "zenodo_archive":{"bytes":4603,"md5":"3493ddfc97b01bb9c94cf38050a26287","sha256_prepared":"2017f00f03c3d6af356db064e4e3f16e399d30bd4625335a9bfc0939927f3cd3"},
 "verification_url":"https://zippri.com/agastya-native-brain-evidence/f3-8b/#verify",
 "disclaimer":"Publisher-issued evidence statement, not independent third-party certification or proof of model acceptance; PDF integrity is not a cryptographic signature."
}
(ROOT/"certificate-manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
(ROOT/"SHA256SUMS.txt").write_text(sha+"  "+NAME+"\n",encoding="ascii")
print("CERTIFICATE_GENERATED",len(pdf),"SHA256",sha,"PATH",str(ROOT/NAME))
