--I just joined with itself on term. I did not have to compute for all docs. It worked!
--I guess joining with itself is transposing.

select a.docid, b.docid, sum (a.count * b.count) as score
from frequency a, frequency b
where a.term = b.term
--and a.docid < b.docid
and a.docid = '10080_txt_crude'
and b.docid = '17035_txt_earn'
group by a.docid, b.docid
;

If we would like to get the sum per term:

select a.docid, b.docid, b.term, sum (a.count * b.count) as score
from frequency a, frequency b
where a.term = b.term
--and a.docid < b.docid
and a.docid = '10080_txt_crude'
and b.docid = '17035_txt_earn'
group by a.docid, b.docid, b.term
;
