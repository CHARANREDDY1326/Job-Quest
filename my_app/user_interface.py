from .job_match_engine import JobMatchEngine
from job.models import Job
class UserInterface:
    def __init__(self):
        pass

    def get_jobs(self):
            return Job.objects.filter(is_available=True),[job.title for job in Job.objects.filter()]
    # def add_candidate(self, name, skills):
    #     """
    #     Add a new candidate to the system.

    #     Args:
    #         name (str): Name of the candidate.
    #         skills (str): Skills possessed by the candidate.
    #     """
    #     self.candidate_database.add_candidate(name, skills)

    def match_candidates_to_jobs(self,request):
        from resume.models import Resume
        """
        Match candidates to available jobs and store the results.
        """

        results = JobMatchEngine.match_jobs(request)
        better_jobs = []
        for result in results:
                # print(f" - {job.title} (Similarity Score: {similarity_score})")

                if(result[1] > 0.3):
                    # print('similarity_Score',result[1])
                    better_jobs.append(result[0])
        # print(better_jobs)
        return better_jobs
        return results
