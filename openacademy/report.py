from odoo import api, models


class ReportSession(models.AbstractModel):
    _name = "report.openacademy.report_session"

    @api.multi
    def render_html(self, docids, data=None):
        report_obj = self.env["report"]
        report = report_obj._get_report_from_name("openacademy.report_session")
        docargs = {
            "doc_ids": docids,
            "doc_model": report.model,
            "docs": self.env['openacademy.session'].browse(docids),
            "other_variable": 'other value'
        }
        return report_obj.render("openacademy.report_session_view", docargs)