from .nlp_utils import preprocess_text, calculate_text_similarity
from job.models import Job
from resume.models import Resume
class JobMatchEngine:
    def __init__(self):
        pass

    def match_jobs(request):

        resume = Resume.objects.get(user_id=request.user.id)
        # print(resume)
        
        candidate_skills = preprocess_text(str(resume.skills))
        # print(Resume.objects.filter()[1:])
        job_matches = []
        # temp_jobs=[]
        for job in Job.objects.filter(is_available=True):
            job_skills = preprocess_text(str(job.skills))
            print(candidate_skills)
            print('This is job_skills')
            print(job_skills)
            # print(job_skills)
            similarity_score = calculate_text_similarity(" ".join(candidate_skills), " ".join(job_skills))
            # print(job,similarity_score)
            # print(job,similarity_score)
            job_matches.append((job, similarity_score))
            print(similarity_score)
            # print(job_matches)
            # temp_jobs.append(job)
        return sorted(job_matches, key=lambda x: x[1], reverse=True)
        return temp_jobs

