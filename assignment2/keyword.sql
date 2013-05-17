--Both yield same results

select docid, sum(count) cnt from frequency where term in ('washington', 'taxes', 'treasury') group by docid order by cnt desc;

select a.docid, sum (a.count * b.count) as score
from frequency a, 
(
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
) b
where a.term = b.term
group by a.docid, b.docid
order by score desc
;

select a.docid, a.term, sum (a.count * b.count) as score
from frequency a, 
(
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
) b
where a.term = b.term
group by a.docid, b.docid, a.term
order by score desc
;