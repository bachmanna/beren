# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .endpoints import (
    OrthancInstances,
    OrthancModalities,
    OrthancPatients,
    OrthancQueries,
    OrthancSeries,
    OrthancServer,
    OrthancStudies,
)
from json import dumps
from warnings import warn
from urllib.parse import urlparse

__all__ = ["Orthanc"]


class Orthanc:
    def __init__(self, server, auth=None):
        self._target = server
        self._auth = auth
        self.instances = OrthancInstances
        self.modalities = OrthancModalities
        self.patients = OrthancPatients
        self.queries = OrthancQueries
        self.series = OrthancSeries
        self.server = OrthancServer
        self.studies = OrthancStudies

        if urlparse(server)[0] == "http":
            warn(
                """{} is an unencrypted connection! Strongly consider using an encrypted (https) REST endpoint.""".format(
                    server
                )
            )

        # Set target for each apiron service
        for x in [
            self.instances,
            self.modalities,
            self.patients,
            self.queries,
            self.series,
            self.server,
            self.studies,
        ]:
            setattr(x, "domain", self._target)

    def __repr__(self):
        return "<Orthanc REST client({})>".format(self._target)

    @staticmethod
    def convert_to_json(data, **kwargs):
        return dumps(data, **kwargs)

    #### INSTANCES
    def get_instances(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.instances(**kwargs)

    def add_instance(self, dicom, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.add_instance(data=dicom, **kwargs)

    def get_instance(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.instance(id_=id_, **kwargs)

    def delete_instance(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.del_instance(id_=id_, **kwargs)

    def anonymize_instance(self, id_, data={}, **kwargs):
        j = self.convert_to_json(data)
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.anonymize(id_=id_, data=j, **kwargs)

    def get_instance_content(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.content(id_=id_, **kwargs)

    def get_instance_content_raw_tag(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.content_raw_tag(id_=id_, **kwargs)

    def export_instance(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.export(id_=id_, data={}, **kwargs)

    def get_instance_file(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.file_(id_=id_, **kwargs)

    def get_instance_frames(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.frames(id_=id_, **kwargs)

    def get_instance_frame_int16(self, id_, frame, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.frame_int16(id_=id_, number=frame, **kwargs)

    def get_instance_frame_uint16(self, id_, frame, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.frame_uint16(id_=id_, number=frame, **kwargs)

    def get_instance_frame_uint8(self, id_, frame, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.frame_uint8(id_=id_, number=frame, **kwargs)

    def get_instance_frame_matlab(self, id_, frame, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.frame_matlab(id_=id_, number=frame, **kwargs)

    def get_instance_frame_preview(self, id_, frame, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.frame_preview(id_=id_, number=frame, **kwargs)

    def get_instance_frame_raw(self, id_, frame, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.frame_raw(id_=id_, number=frame, **kwargs)

    def get_instance_frame_raw_gz(self, id_, frame, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.frame_raw_gz(id_=id_, number=frame, **kwargs)

    def get_instance_header(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.header(id_=id_, **kwargs)

    def get_instance_int16(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.image_int16(id_=id_, **kwargs)

    def get_instance_uint16(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.image_uint16(id_=id_, **kwargs)

    def get_instance_uint8(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.image_uint8(id_=id_, **kwargs)

    def get_instance_matlab(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.matlab(id_=id_, **kwargs)

    def modify_instance(self, id_, data, **kwargs):
        j = self.convert_to_json(data)
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.modify(id_=id_, data=j, **kwargs)

    def get_instance_module(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.module(id_=id_, **kwargs)

    def get_instance_patient(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.patient(id_=id_, **kwargs)

    def get_instance_pdf(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.pdf(id_=id_, **kwargs)

    def get_instance_preview(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.preview(id_=id_, **kwargs)

    def reconstruct_instance(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.reconstruct(id_=id_, data={}, **kwargs)

    def get_instance_series(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.series(id_=id_, **kwargs)

    def get_instance_simplified_tags(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.simplified_tags(id_=id_, **kwargs)

    def get_instance_statistics(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.statistics(id_=id_, **kwargs)

    def get_instance_study(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.study(id_=id_, **kwargs)

    def get_instance_tags(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.instances.tags(id_=id_, **kwargs)

    #### PATIENTS
    def get_patients(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.patients(**kwargs)

    def get_patient(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.patient(id_=id_, **kwargs)

    def delete_patient(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.del_patient(id_=id_, **kwargs)

    def anonymize_patient(self, id_, data={}, **kwargs):
        j = self.convert_to_json(data)
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.anonymize(id_=id_, data=j, **kwargs)

    def archive_patient(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.archive(id_=id_, **kwargs)

    def get_patient_instances(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.instances(id_=id_, **kwargs)

    def get_patient_instance_tags(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.instances_tags(id_=id_, **kwargs)

    def modify_patient(self, id_, data, **kwargs):
        j = self.convert_to_json(data)
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.modify(id_=id_, data=j, **kwargs)

    def get_patient_module(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.module(id_=id_, **kwargs)

    def get_patient_media(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.media(id_=id_, **kwargs)

    def get_patient_protected(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.protected(id_=id_, **kwargs)

    def put_patient_protected(self, id_, data={}, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.put_protected(id_=id_, data=data, **kwargs)

    def reconstruct_patient(self, id_, data={}, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.protected(id_=id_, data=data, **kwargs)

    def get_patient_series(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.series(id_=id_, **kwargs)

    def get_patient_shared_tags(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.shared_tags(id_=id_, **kwargs)

    def get_patient_statistics(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.statistics(id_=id_, **kwargs)

    def get_patient_studies(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.patients.studies(id_=id_, **kwargs)

    def get_patient_id_from_uuid(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return (
            self.patients.patient(id_=id_, **kwargs)
            .get("MainDicomTags")
            .get("Patientid_")
        )

    def get_patient_studies_from_id(self, id_, **kwargs):
        try:
            kwargs["auth"] = kwargs.get("auth", self._auth)
            return [
                self.get_patient_studies(patient)
                for patient in self.find(
                    {"Level": "Patient", "Limit": 1, "Query": {"Patientid_": id_}},
                    **kwargs
                )
            ][0]
        except:
            return []

    #### QUERIES
    def get_queries(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.queries.queries(**kwargs)

    def get_query(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.queries.query(id_=id_, **kwargs)

    def delete_query(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.queries.del_query(id_=id_, **kwargs)

    def get_query_answers(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.queries.query(id_=id_, **kwargs)

    def get_query_answers_content(self, id_, index, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.queries.answers_content(id_=id_, index=index, **kwargs)

    def post_query_answers_retrieve(self, id_, index, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.queries.answers_retrieve(id_=id_, index=index, **kwargs)

    def get_query_level(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.queries.level(id_=id_, **kwargs)

    def get_query_modality(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.queries.modality(id_=id_, **kwargs)

    def get_query_query(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.queries.query_query(id_=id_, **kwargs)

    def post_query_retrieve(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.queries.retrieve(id_=id_, **kwargs)

    #### SERIES
    def get_series(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.series(**kwargs)

    def get_one_series(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.part(id_=id_, **kwargs)

    def delete_series(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.del_part(id_=id_, **kwargs)

    def anonymize_series(self, id_, data={}, **kwargs):
        j = self.convert_to_json(data)
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.anonymize(id_=id_, data=j, **kwargs)

    def get_series_archive(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.archive(id_=id_, **kwargs)

    def get_series_instances(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.instances(id_=id_, **kwargs)

    def get_series_instances_tags(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.instances_tags(id_=id_, **kwargs)

    def get_series_media(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.media(id_=id_, **kwargs)

    def modify_series(self, id_, data, **kwargs):
        j = self.convert_to_json(data)
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.modify(id_=id_, data=j, **kwargs)

    def get_series_module(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.module(id_=id_, **kwargs)

    def get_series_ordered_slices(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.ordered_slices(id_=id_, **kwargs)

    def get_series_patient(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.patient(id_=id_, **kwargs)

    def reconstruct_series(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.reconstruct(id_=id_, **kwargs)

    def get_series_shared_tags(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.shared_tags(id_=id_, **kwargs)

    def get_series_statistics(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.statistics(id_=id_, **kwargs)

    def get_series_study(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.series.study(id_=id_, **kwargs)

    #### STUDIES
    def get_studies(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.studies(**kwargs)

    def get_study(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.study(id_=id_, **kwargs)

    def delete_study(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.del_study(id_=id_, **kwargs)

    def anonymize_study(self, id_, data={}, **kwargs):
        j = self.convert_to_json(data)
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.anonymize(id_=id_, data=j, **kwargs)

    def get_study_archive(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.archive(id_=id_, **kwargs)

    def get_study_instances(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.instances(id_=id_, **kwargs)

    def get_study_instances_tags(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.instances_tags(id_=id_, **kwargs)

    def get_study_media(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.media(id_=id_, **kwargs)

    def modify_study(self, id_, data, **kwargs):
        j = self.convert_to_json(data)
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.modify(id_=id_, data=j, **kwargs)

    def get_study_module(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.module(id_=id_, **kwargs)

    def get_study_module_patient(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.module_patient(id_=id_, **kwargs)

    def get_study_patient(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.patient(id_=id_, **kwargs)

    def reconstruct_study(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.reconstruct(id_=id_, **kwargs)

    def get_study_series(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.series(id_=id_, **kwargs)

    def get_study_shared_tags(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.shared_tags(id_=id_, **kwargs)

    def get_study_statistics(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.studies.statistics(id_=id_, **kwargs)

    #### MODALITIES ###
    def get_modalities(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.modalities.modalities(**kwargs)

    def get_modality(self, dicom, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.modalities.modality(dicom=dicom, **kwargs)

    def delete_modality(self, dicom, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.modalities.del_modality(dicom=dicom, **kwargs)

    def update_modality(self, dicom, data, **kwargs):
        j = self.convert_to_json(data)
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.modalities.put_modality(dicom=dicom, data=j, **kwargs)

    def echo_modality(self, dicom, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.modalities.echo(dicom=dicom, data={}, **kwargs)

    def move_modality(self, dicom, data, **kwargs):
        j = self.convert_to_json(data)
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.modalities.move(dicom=dicom, data=j, **kwargs)

    def query_modality(self, dicom, data, **kwargs):
        j = self.convert_to_json(data)
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.modalities.query(dicom=dicom, data=j, **kwargs)

    def store_modality(self, dicom, data, **kwargs):
        j = self.convert_to_json(data)
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.modalities.store(dicom=dicom, data=j, **kwargs)

    #### SERVER-RELATED
    def get_changes(self, since=0, limit=100, last=False, **kwargs):
        if last:
            kwargs["params"] = {"last": ""}  # overrule
        else:
            kwargs["params"] = {"since": since, "limit": limit}  # overrule
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.changes(**kwargs)

    def clear_changes(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.del_changes(**kwargs)

    def get_exports(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.exports(**kwargs)

    def clear_exports(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.del_exports(**kwargs)

    def get_jobs(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.jobs(**kwargs)

    def get_job(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.job(id_=id_, **kwargs)

    def cancel_job(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.cancel_job(id_=id_, data={}, **kwargs)

    def pause_job(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.pause_job(id_=id_, data={}, **kwargs)

    def resubmit_job(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.resubmit_job(id_=id_, data={}, **kwargs)

    def resume_job(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.resume_job(id_=id_, data={}, **kwargs)

    def get_peers(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.peers(**kwargs)

    def get_peer(self, peer, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.peer(peer=peer, **kwargs)

    def delete_peer(self, peer, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.del_peer(peer=peer, **kwargs)

    def put_peer(self, peer, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.put_peer(peer=peer, **kwargs)

    def store_peer(self, peer, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.store_peer(peer=peer, **kwargs)

    def get_plugins(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.plugins(**kwargs)

    def get_plugin(self, id_, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.plugin(id_=id_, **kwargs)

    def get_plugins_js(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.plugins_js(**kwargs)

    def get_statistics(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.statistics(**kwargs)

    def get_system(self, **kwargs):
        """Get running system information

        :return:
            System information
        :rtype:
            dict
        """
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.system(**kwargs)

    def create_archive(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_create_archive(**kwargs)

    def create_dicom(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_create_dicom(**kwargs)

    def create_media(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_create_media(**kwargs)

    def create_media_extended(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_create_media_extended(**kwargs)

    def get_default_encoding(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_default_encoding(**kwargs)

    def change_default_encoding(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_post_default_encoding(**kwargs)

    def get_dicom_conformance(self, **kwargs):
        """Get the DICOM conformance statement of this version of Orthanc

        :return:
            DICOM conformance statement
        :rtype:
            str
        """
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_dicom_conformance(**kwargs)

    def execute_script(self, script, **kwargs):
        j = self.convert_to_json(script)
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_execute_script(data=j, **kwargs)

    def find(self, query, **kwargs):
        """Run C-Find with query

        Example: query = {'Level': 'Patient', 'Query': {'PatientName': 'John*'}}

        :param dict query:
            Query to run
        :return:
            Matching record uuid(s)
        :rtype:
            list
        """
        j = self.convert_to_json(query)
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_find(data=j, **kwargs)

    def generate_uid(self, level, **kwargs):
        """Generate DICOM UID

        :param str level:
            DICOM UID level (patient, series, study, or instance)
        :return:
            UID
        :rtype:
            str
        """
        if level not in ["patient", "instance", "series", "study"]:
            raise ValueError("Must be patient, instance, series, or study")
        params = {"level": level}
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_generate_uid(params=params, **kwargs)

    def invalidate_tags(self, **kwargs):
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_invalidate_tags(**kwargs)

    def lookup(self, lookup, **kwargs):
        """Map DICOM UIDs to Orthanc identifiers

        :param lookup:
            UID(s) to map
        :return:
            Orthanc identifiers
        :rtype:
            list
        """
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_lookup(data=self.convert_to_json(lookup), **kwargs)

    def get_now(self, **kwargs):
        """Get the current universal datetime (UTC) in the ISO 8601 format

        :return:
            Universal datetime (UTC)
        :rtype:
            str (ISO 8601)
        """
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_now(**kwargs)

    def get_now_local(self, **kwargs):
        """Get the current local datetime in the ISO 8601 format

        :return:
            Local datetime
        :rtype:
            str (ISO 8601)
        """
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_now_local(**kwargs)

    def reconstruct(self, **kwargs):
        """Reconstruct the main DICOM tags, JSON summary, and metadata of all instances. Slow!

        :return:
            Empty string on success or raises Exception
        :rtype:
            str
        """
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_reconstruct(data={}, **kwargs)

    def reset(self, **kwargs):
        """Hot restart of Orthanc server and re-reads configuration file

        :return:
            Empty dict on success or raises Exception
        :rtype:
            dict
        """
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_reset(data={}, **kwargs)

    def shutdown(self, **kwargs):
        """Stop Orthanc server

        :return:
            Empty list on success
        :rtype:
            dict
        """
        kwargs["auth"] = kwargs.get("auth", self._auth)
        return self.server.tools_shutdown(data={}, **kwargs)
